#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Traveler, Island, Vacation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Welcome to the API, available resources include /travelers and /islands"

# --- TRAVELER ROUTES --- #

# GET - INDEX (ALL)
@app.get('/travelers')
def travelers():
    all_travelers = Traveler.query.all()
    return [ traveler.to_dict() for traveler in all_travelers  ], 200

# GET - FIND BY ID (SHOW)
@app.get('/travelers/<int:id>')
def get_traveler_by_id(id):
    found_traveler = Traveler.query.where(Traveler.id == id).first()

    if found_traveler:
        return found_traveler.to_dict(rules=("islands",)), 200
    
    else:
        return { "error": "Not found" }, 404

# POST - CREATE
@app.post('/travelers')
def post_travelers():
    data = request.json

    try:
        new_traveler = Traveler(name=data.get("name"), age=data.get("age"), budget=data.get("budget"), frequent_flyer=data.get("frequent_flyer"))

        db.session.add(new_traveler)
        db.session.commit()
        return new_traveler.to_dict(), 201
    
    except:
        return { "error": "Invalid traveler" }, 406

# PATCH - UPDATE
@app.patch('/travelers/<int:id>')
def update_traveler(id):
    data = request.json
    found_traveler = Traveler.query.where(Traveler.id == id).first()

    if found_traveler:
        try:
            for key in data:
                setattr(found_traveler, key, data[key])

            db.session.commit()
            return found_traveler.to_dict(), 202

        except:
            return { "error": "Invalid traveler" }, 406

    else:
        return { "error": "Not found" }, 404


# DELETE - DESTROY BY ID
@app.delete('/travelers/<int:id>')
def delete_traveler(id):
    found_traveler = Traveler.query.where(Traveler.id == id).first()

    if found_traveler:
        db.session.delete(found_traveler)
        db.session.commit()
        return {}, 204
    else:
        return { "error": "Not found" }, 404


# --- ISLAND ROUTES --- #

# GET - INDEX (ALL)
@app.get('/islands')
def islands():
    all_islands = Island.query.all()
    return [ island.to_dict() for island in all_islands  ], 200

# GET - FIND BY ID (SHOW)
@app.get('/islands/<int:id>')
def get_island_by_id(id):
    found_island = Island.query.where(Island.id == id).first()

    if found_island:
        return found_island.to_dict(), 200
    
    else:
        return { "error": "Not found" }, 404

# POST - CREATE

# PATCH - UPDATE

# DELETE - DESTROY BY ID
    
# --- VACATION ROUTES --- #

# GET - INDEX (ALL)
@app.get('/vacations')
def vacations():
    all_vacations = Vacation.query.all()
    return [ vacation.to_dict() for vacation in all_vacations  ], 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
