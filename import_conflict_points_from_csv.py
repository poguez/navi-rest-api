from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models_postgis import ConflictPoint

engine = create_engine('postgresql://postgres:postgres@localhost:5432/navi_voice_assistant', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


lake = ConflictPoint(borough='Manhattan', risk=12, geom='POINT(-73.9745 40.7585)')
session.add(lake)
session.commit()

