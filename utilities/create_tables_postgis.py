from models_postgis import ConflictPoint
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/gis', echo=True)

ConflictPoint.__table__.create(engine)