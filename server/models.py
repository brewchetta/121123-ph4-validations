from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# Traveler -----< Vacations >----- Island #


class Traveler(db.Model, SerializerMixin):
    __tablename__ = "travelers_table"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    budget = db.Column(db.Integer)
    frequent_flyer = db.Column(db.Boolean)

    vacations = db.relationship("Vacation", back_populates="traveler")
    islands = association_proxy("vacations", "island")

    serialize_rules = ("-vacations",)


class Island(db.Model, SerializerMixin):
    __tablename__ = "islands_table"
    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False, unique=True)
    square_miles = db.Column(db.Integer)
    average_temperature = db.Column(db.Integer)

    vacations = db.relationship("Vacation", back_populates="island")
    travelers = association_proxy("vacations", "traveler")

    serialize_rules = ("-vacations.island",)
    

class Vacation(db.Model, SerializerMixin):
    __tablename__ = "vacations_table"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    description = db.Column(db.String)

    traveler_id = db.Column(db.Integer, db.ForeignKey('travelers_table.id'))
    island_id = db.Column(db.Integer, db.ForeignKey('islands_table.id'))

    island = db.relationship("Island", back_populates="vacations")
    traveler = db.relationship("Traveler", back_populates="vacations")
    
    serialize_rules = ("-traveler", "-island")