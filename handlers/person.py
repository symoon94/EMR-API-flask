
from flask import request
from flask import jsonify
from sqlalchemy import func, case, and_

from app import app

from models.models import Person, Death, Visit

import json
import time
from collections import defaultdict


def create_ages_visit(person_query, Visit, year):
    dic = defaultdict(int)
    current_year = time.localtime().tm_year
    for i in range(0, 130, 10):
        dic[i] = person_query.join(Visit).filter(
            and_(current_year-year >= i, current_year-year < i+10)).count()
    return dic


@app.route('/person')
def get_person():
    if request.method == 'GET':
        person_query = app.db.query(Person)

        gender = Person.gender_concept_id
        race = Person.race_concept_id
        ethnicity = Person.ethnicity_concept_id

        gender = person_query.with_entities(
            gender, func.count(gender)).group_by(gender).all()
        race = person_query.with_entities(
            race, func.count(race)).group_by(race).all()
        ethnicity = person_query.with_entities(
            ethnicity, func.count(ethnicity)).group_by(ethnicity).all()

        gender = json.loads(json.dumps(dict(gender)))
        race = json.loads(json.dumps(dict(race)))
        ethnicity = json.loads(json.dumps(dict(ethnicity)))

        death = app.db.query(Death).count()

        return jsonify({"total": person_query.count(), "gender": gender, "race": race, "ethnicity": ethnicity, "death": death})


@ app.route('/visit')
def get_visit():
    if request.method == 'GET':
        visit_query = app.db.query(Visit)
        person_query = app.db.query(Person)

        visit = Visit.visit_concept_id
        gender = Person.gender_concept_id
        race = Person.race_concept_id
        ethnicity = Person.ethnicity_concept_id
        year = Person.year_of_birth

        visit = visit_query.with_entities(visit, func.count(
            visit)).group_by(visit).all()
        gender_visit = person_query.join(Visit).with_entities(
            gender, func.count(gender)).group_by(gender).all()
        race_visit = person_query.join(Visit).with_entities(
            race, func.count(race)).group_by(race).all()
        ethnicity_visit = person_query.join(Visit).with_entities(
            ethnicity, func.count(ethnicity)).group_by(ethnicity).all()
        ages_visit = create_ages_visit(person_query, Visit, year)

        visit = json.loads(json.dumps(dict(visit)))
        gender_visit = json.loads(json.dumps(dict(gender_visit)))
        race_visit = json.loads(json.dumps(dict(race_visit)))
        ethnicity_visit = json.loads(json.dumps(dict(ethnicity_visit)))
        ages_visit = json.loads(json.dumps(ages_visit))

        return jsonify({"visit_type": visit, "gender_visit_occurence": gender_visit, "race_visit_occurence": race_visit, "ethnicity_visit_occurence": ethnicity_visit, "ages_visit_occurence": ages_visit})


@ app.route('/api')
def get_api():
    if request.method == 'GET':
        return jsonify({"count": 'tmp'})
