from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models_postgis import ConflictPoint
import csv

engine = create_engine('postgresql://postgres:postgres@localhost:5432/navi_voice_assistant', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

with open('risk_points.csv', 'rb') as csvfile:
    risk_points_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in risk_points_reader:
        # print ', '.join(row)
        geometry_value = "POINT(%s %s)" % (row['latitude'], row['longitude'])
        risk_value = int(row['risk'])
        lake = ConflictPoint(borough='Manhattan', risk=risk_value, geom=geometry_value)
        session.add(lake)
        session.commit()