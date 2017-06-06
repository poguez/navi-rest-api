from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

engine = create_engine('postgresql://postgres:postgres@localhost:5432/gis', echo=True)

Base = declarative_base()

class ConflictPoint(Base):
    __tablename__ = 'conflict_point'
    id = Column(Integer, primary_key=True)
    borough = Column(String)
    risk = Column(Integer)
    geom = Column(Geometry('POINT'))