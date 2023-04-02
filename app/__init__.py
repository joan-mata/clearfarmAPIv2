from flask import Flask, session
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
#db_users = client.users

#db_cows = client["tests"]
db_cows = client["cows"] #real cows
db_pigs = client["pigs"] #real pigs
db_users = client["users"] #real users


def create_app():
    #ALLOWED_EXTENSIONS = set(['csv', 'json'])

    app = Flask(__name__)
    #app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = "abcd1234"
    
    #db.init_app(app)

    # Registro de los Blueprints
    from .dbtest import dbtest_bp
    app.register_blueprint(dbtest_bp)
    
    from .home import home_bp
    app.register_blueprint(home_bp)
    
    from .inserts import inserts_bp
    app.register_blueprint(inserts_bp)
    
    from .msg import msg_bp
    app.register_blueprint(msg_bp)
    
    from .search import search_bp
    app.register_blueprint(search_bp)
    
    from .welfare import welfare_bp
    app.register_blueprint(welfare_bp)
    
    return app
    


msg_dict = {
    "error_required_animal": {
        "type": "error",
        "name": "error_required_animal",
        "text": "Is required the 'animal' value.",
    },
    "error_required_farmId": {
        "type": "error",
        "name": "error_required_farmId",
        "text": "Is required the 'farmId' value or the value is not a integer.",
    },
    "error_value_farmId": {
        "type": "error",
        "name": "error_value_farmId",
        "text": "Value is smaller than 1.",
    },
    "error_required_animalId": {
        "type": "error",
        "name": "error_required_animalId",
        "text": "Is required the 'animalId' value because you have inserted the 'animalNum' value.",
    },
    "error_value_animalId": {
        "type": "error",
        "name": "error_value_animalId",
        "text": "It is possible that you have not correctly selected the 'AnimalId' value.",
    },
    "error_format_timeFrom": {
        "type": "error",
        "name": "error_format_timeFrom",
        "text": "Format of 'timeFrom' is not correct. Correct format is 'YYYY-MM-DD'.",
    },
    "error_format_timeTo": {
        "type": "error",
        "name": "error_format_timeTo",
        "text": "Format of 'timeTo' is not correct. Correct format is 'YYYY-MM-DD'.",
    },
    "error_today_timeFrom": {
        "type": "error",
        "name": "error_today_timeFrom",
        "text": "'timeFrom' value must be smaller than today's date."
    },
    "error_today_timeTo": {
        "type": "error",
        "name": "error_today_timeTo",
        "text": "'timeTo' value must be smaller than today's date."
    },
    "error_small_timeTo": {
        "type": "error",
        "name": "error_small_timeTo",
        "text": "'timeTo' value must be greater than 'timeFrom' value."
    },
    "error_no_post": {
        "type": "error",
        "name": "error_no_post",
        "text": "You do not use a POST method",
    },
    "no_data_animalNum": {
        "type": "information",
        "name": "no_data_animalNum",
        "text": "No information about this animal in this farm."
    },
    "ok_insert": {
        "type": "information",
        "name": "ok_insert",
        "text": "Your POST method have been sent correctly."
    }

}
    
        
    
