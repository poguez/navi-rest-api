import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#
#   UserMeasurement
#
#   A Model for saving a UserMeasurement history of the user
#       id: (Auto generated) Unique id.
#       username: The name of the user to identify who is measuring.
#       speed: The speed vector.
#       bearing: The direction of the measurement.
#       location: Geolocalization of the user.
#       mode_of_transportation: The mode of transportation provided by the user.
#       timestamp: (Auto generated) UTC time stamp of the event
#

class UserMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(64), nullable=False, index=True)
    speed = db.Column(db.String(64), nullable=False, index=True)
    bearing= db.Column(db.Float, nullable=False)
    latitude = db.Column(db.String(64), index=True, nullable=False)
    longitude = db.Column(db.String(64), index=True, nullable=False)
    mode_of_transportation = db.Column(db.String(64), index=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

#
#   AlertSent
#
#   A Model for saving an Alert Sent to the user with
#
#       id: (Auto generated) Unique id.
#       username: The name of the user to identify who is measuring.
#       location: Geolocalization of the user.
#       mode_of_transportation: The mode of transportation provided by the user.
#       warning_text: The text generated to alert the driver.
#       timestamp: (Auto generated) UTC time stamp of the event
#

class AlertSent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True)
    location = db.Column(db.String(64), index=True, nullable=False)
    mode_of_transportation = db.Column(db.String(64), index=True, nullable=False)
    warning_text = db.Column(db.String)
    timestamp =db.Column(db.DateTime, default=datetime.datetime.utcnow)