
from flask import request
from flask import jsonify
from sqlalchemy import func

from app import app

from models.models import Person, Death, Visit

import json


@app.route('/person')
def get_person():
    if request.method == 'GET':
        query = app.db.query(Person)

        gender = Person.gender_concept_id
        race = Person.race_concept_id
        ethnicity = Person.ethnicity_concept_id

        gender = query.with_entities(
            gender, func.count(gender)).group_by(gender).all()
        race = query.with_entities(race, func.count(race)).group_by(race).all()
        ethnicity = query.with_entities(
            ethnicity, func.count(ethnicity)).group_by(ethnicity).all()

        gender = json.loads(json.dumps(dict(gender)))
        race = json.loads(json.dumps(dict(race)))
        ethnicity = json.loads(json.dumps(dict(ethnicity)))

        death = app.db.query(Death).count()

        return jsonify({"total": query.count(), "gender": gender, "race": race, "ethnicity": ethnicity, "death": death})


@ app.route('/visit')
def get_visit():
    if request.method == 'GET':
        query = app.db.query(Visit)

        visit = Visit.visit_concept_id

        visit = query.with_entities(visit, func.count(
            visit)).group_by(visit).all()

        visit = json.loads(json.dumps(dict(visit)))

        return jsonify(visit)


@ app.route('/api')
def get_api():
    if request.method == 'GET':
        return jsonify({"count": 'tmp'})
