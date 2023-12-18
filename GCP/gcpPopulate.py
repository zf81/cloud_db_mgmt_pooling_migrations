import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
from gcpDatabase import Patient, LaboratoryOrder
import random

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_GCP = os.getenv("GCPURL")


# Create a database engine
engine = create_engine(DB_GCP, echo=False)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

#create a faker instance 
fake = Faker()

for _ in range(10):
    patient = Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(minimum_age=10, maximum_age=100),
        contact_number = fake.phone_number()
    )
    session.add(patient)

for _ in range(20):
    laborder = LaboratoryOrder(
        lab_name=fake.first_name(),
        lab_date=fake.date_between(start_date="-5y", end_date="today"),
        lab_result=fake.random_element(elements=('Abnormal', 'Normal')),
        lab_id=session.query(Patient).order_by(func.rand()).first().id
    )
    session.add(laborder)

#commit
session.commit()

#close session 
session.close()