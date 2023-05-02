from flask import Flask

from .. import disease_bp
from ..functions import funct_disease
    
@disease_bp.route('/disease/mastitis')
def disease_mastitis():
    '''
    Search and return data range for MASTITIS score of animal
    
    Args: {
        animal: {   def: "is the type of animal we want search.",
                    type: string,
                    required: yes,
                    default: 'none',
                    values: ['cow', 'pig']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: int,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
        timeFrom: { def: "lower limit for the range of dates where we want to search information",
                    type: string,
                    required: no,
                    format date: 'YYYY-MM-DD',
                    default: 'none',
                    values: date,
                    comment: "If you insert any value in 'timeFrom', the 'quantity' value are not important, because change automaticaly to 'Range'."
                },
        timeTo: {   def: "upper limit for the range of dates where we want to search information",
                    type: string,
                    required: no,
                    format date: 'YYYY-MM-DD',
                    default: 'none',
                    values: "any date greater than 'timeFrom' and smaller than today",
                    comment: "If you do not insert any value in 'timeFrom', the 'timeTo' does not work."
                },
    }
    '''
    
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalNum = str(request.args.get('animalNum', default = 0, type = int))
    timeFrom = request.args.get('timeFrom', default = 'none', type = str)
    timeTo = request.args.get('timeTo', default = 'none', type = str)
    
    value_return = funct_disease.funct_disease("mastitis", animal, farmId, animalNum, timeFrom, timeTo)
    
    return value_return
    
    
    return return_value

            
@disease_bp.route('/disease/acitosis')
def disease_acitosis():
    '''
    '''
    return return_value

@disease_bp.route('/disease/pneumonia')
def disease_pneumonia():
    '''
    '''
    return return_value
    
@disease_bp.route('/disease/abomasus_surgery')
def disease_abomasus_surgery():
    '''
    '''
    return return_value

@disease_bp.route('/disease/all')
def disease_all():
    '''
    '''
    return return_value