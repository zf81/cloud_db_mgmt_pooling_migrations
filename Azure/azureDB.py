"""

pip install sqlalchemy alembic mysql-connector-python
pip install pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their preferences:

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

AZUREURL = os.getenv("AZUREURL")

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    contact_number = Column(String(50), nullable=False)
    happiness_score = Column(Integer)
    sadness_score = Column(Integer)
    favorite_tv_show = Column(String(50), nullable=False)
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


connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(AZUREURL,
    connect_args={'ssl': {'ssl-mode':'preferred'}},
)   

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)
