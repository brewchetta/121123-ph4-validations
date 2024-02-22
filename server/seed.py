#!/usr/bin/env python3

from app import app
from models import db, Traveler, Island
from faker import Faker
from random import randint, random_choice

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Starting Seed...")

        print("Clearing old data...")
        Traveler.query.delete()
        Island.query.delete()

        print("Creating travelers...")

        bools = [True, False]

        for _ in range(10):
            t = Traveler(name=faker.name(), age=randint(10, 100), budget=randint(500, 50000), frequent_flyer=random_choice(bools))

            print(f"  Created {t.name}...")
            db.session.add(t)

        db.session.commit()


        print("Creating islands...")

        for _ in range(10):
            i = Island(name=faker.country(), square_miles=randint(1, 500), average_temperature=randint(70, 100))

            print(f"  Created {i.name}...")
            db.session.add(i)

        db.session.commit()

        print("Seeding complete!")
