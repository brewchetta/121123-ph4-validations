from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Traveler(db.Model):
    pass

    # ATTRIBUTES #

    # id - Integer
    # name - String - required
    # age - Integer
    # budget - Integer
    # frequent_flyer - Boolean

class Island(db.Model):
    pass

    # ATTRIBUTES #

    # id - Integer
    # name - String - required and unique
    # square_miles - Integer
    # average_temperature - Integer