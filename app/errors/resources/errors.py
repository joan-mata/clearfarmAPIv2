from flask import Flask

from .. import errors_bp


@errors_bp.route('/errors')
def errors():
    '''
    List of errors
    
    Args:
        None
    '''
    
    error_dict = {
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
        "no_data_animalNum": {
            "type": "no_data",
            "name": "no_data_animalNum",
            "text": "No information about this animal in this farm"
        },
    }
    
    
    
    return error_dict

            
