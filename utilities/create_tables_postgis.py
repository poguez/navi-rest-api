from models_postgis import ConflictPoint
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/navi_voice_assistant', echo=True)

ConflictPoint.__table__.create(engine)