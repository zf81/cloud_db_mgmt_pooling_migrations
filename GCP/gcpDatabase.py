"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os 
from dotenv import load_dotenv

load_dotenv()
GCPURL = os.getenv("GCPURL")

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    contact_number = Column(String(50), nullable=False)
    allergies = Column(String(100))
    laboratory = relationship('LaboratoryOrder', back_populates='patient')

class LaboratoryOrder(Base):
    __tablename__ = 'laboratory_order'

    id = Column(Integer, primary_key=True)
    lab_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    lab_name = Column(String(100), nullable=False)
    lab_date = Column(Date, nullable=False)
    lab_result = Column(String(100), nullable=False)
    patient = relationship('Patient', back_populates='laboratory')


### Part 2 - initial sqlalchemy-engine to connect to db:

engine = create_engine(GCPURL,
    connect_args={'ssl': {'ssl-mode':'preferred'}},
)   

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)