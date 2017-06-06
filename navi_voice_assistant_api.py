import datetime, sys

from flask import Flask, jsonify, abort, request
from slugify import slugify
from models import UserMeasurement, AlertSent, db

app = Flask(__name__)
app.config ["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432/navi_voice_assistant'
db.init_app(app)


#
#   /sense [POST]
#
#   This route receives a json with the current
#   Navigation information from the user.
#
#   user information should be sent in the format
#    {
#      "username": "john" //(String) you can pick your username an
#                            don't forget to tell me who you are.
#      "speed": 45, //(Int) In Kilometers per hour.
#      "bearing": "45.678", //(Float) direction of movement.
#      "location": "45,45", // (String) Gelocalization.
#      "mode_of_transportation": "car"  // (String)Car,
#    }
#

@app.route('/sense', methods=['POST'])
def create_user_measurement():
    try:
        user_json = request.get_json(force=True)
        print user_json
        if not {"username", "speed", "latitude", "longitude", "bearing", "mode_of_transportation"} <= set(user_json):
            raise ValueError
        user_json["username"] = slugify(user_json["username"])
        user_measurement = UserMeasurement(username=user_json["username"],
                                           speed= user_json["speed"],
                                           bearing= float(user_json["bearing"]),
                                           latitude=user_json["latitude"],
                                           longitude=user_json["longitude"],
                                           mode_of_transportation= user_json["mode_of_transportation"])
        db.session.add(user_measurement)
        db.session.commit()
        our_response = create_demo_alert("no_alert")
        
    except KeyError:
        abort(404)
    except ValueError:
        example_request ={
                            "username": "Mr. Robot",
                            "speed": "45",
                            "bearing": "45.678",
                            "latitude": "45.01225",
                            "longitude": "45.45312",
                            "mode_of_transportation": "car"
                           }
        return "Your request should contain a JSON as like the following example: \n" + str(example_request), 400
                          
    return jsonify(our_response)


#
#   /
#
#   Say Hi, don't be rude.
#

@app.route('/')
def hello_world():
    return jsonify({"message": 'Hello to the future!'})

#
#   /alert
#
#    It creates a dummy response for you.
#
@app.route('/alert', methods=['GET', 'POST'])
def get_demo_alert():
    try:
        our_response = create_demo_alert()
    except KeyError:
        abort(404)
    return jsonify(our_response)
    

def create_demo_alert(alert_type="no_alert"):
    
    alert = {
        "no_alert" : {
        "timestamp": datetime.datetime.now(),
        "warning_text": "Be careful, Minsoo! At 100 meters ahead, you are approaching a dangerous area where there have been many accidents involving pedestrians. The recommended speed is 30 km/h.",
        "risk_level": "none"
        },
        "demo_alert" : {
        "timestamp": datetime.datetime.now(),
        "warning_text": "Be careful, Minsoo! At 100 meters ahead, you are approaching a dangerous area where there have been many accidents involving pedestrians. The recommended speed is 30 km/h.",
        "risk_level": "low"
        }
    }
    
    return alert.get(alert_type)


if __name__ == '__main__':
    # python navi_voice_assistant_api.py createdb
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")
    else:
        app.run(debug=True, host="0.0.0.0")
