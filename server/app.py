#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Traveler, Island

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
    pass

# GET - FIND BY ID (SHOW)

# POST - CREATE

# PATCH - UPDATE

# DELETE - DESTROY BY ID

# --- ISLAND ROUTES --- #

# GET - INDEX (ALL)
@app.get('/islands')
def islands():
    pass

# GET - FIND BY ID (SHOW)

# POST - CREATE

# PATCH - UPDATE

# DELETE - DESTROY BY ID

if __name__ == '__main__':
    app.run(port=5555, debug=True)
