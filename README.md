# Flask RESTful Routing Practice

## Getting Started

Fork and clone the repository. Run `pipenv install` followed by `pipenv shell` and `cd server`. You can run the application with `python app.py`.

## Deliverables

### Build Models

Build out the two models `Traveler` and `Island`. For now there is no relationship between them.

A `Traveler` has these attributes:
```
id - Integer - primary key
name - String - not nullable
age - Integer
budget - Integer
frequent_flyer - Boolean
```
An `Island` has these attributes:
```
id - Integer - primary key
name - String - not nullable and unique
square_miles - Integer
average_temperature - Integer
```

Once you've built the models you ought to initialize, migrate, and upgrade the database.

### Seeding the Database

You already have a prebuilt seed file in `seed.py`. Attempt to run it with `python seed.py`. 

You'll know if your models are working if the seed file runs properly.

### Building the Routes

Inside `app.py` build out your RESTful routes for `Traveler` and `Island`.

The routes will be:

```
GET /travelers
GET /travelers/:id
POST /travelers
PATCH /travelers/:id
DELETE /travelers/:id

GET /islands
GET /islands/:id
POST /islands
PATCH /islands/:id
DELETE /islands/:id
```

Be sure to test your routes with Postman. 

Additionally, be sure to account for certain events like invalid data or objects not found with the proper status codes!