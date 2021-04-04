
from flask import request

from app import app
from models.person import Person
from sqlalchemy import func
import json
from flask import jsonify


@app.route('/person')
def get_person():
    if request.method == 'GET':
        query = app.db.query(Person)

        gender = query.with_entities(Person.gender_concept_id, func.count(Person.gender_concept_id)).group_by(Person.gender_concept_id).all()
        race =  query.with_entities(Person.race_concept_id, func.count(Person.race_concept_id)).group_by(Person.race_concept_id).all()
        ethnicity = query.with_entities(Person.ethnicity_concept_id, func.count(Person.ethnicity_concept_id)).group_by(Person.ethnicity_concept_id).all()
        
        gender = json.loads(json.dumps(dict(gender)))
        race = json.loads(json.dumps(dict(race)))
        ethnicity = json.loads(json.dumps(dict(ethnicity)))

        return jsonify({"total": query.count(), "gender":gender, "race":race, "ethnicity":ethnicity})

@app.route('/api')
def get_api():
    if request.method == 'GET':
        return jsonify({"count":'tmp'})