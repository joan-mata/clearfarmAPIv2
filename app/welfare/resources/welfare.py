from flask import Flask, request

from .. import welfare_bp
from ..functions import funct_welfare


@welfare_bp.route('/welfare/health')
def wf_health():
    '''
    Search and return data range for HEALTH score of an animal.
    
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
    #Check values we need
    #Values are required: animal, farmId, *animalId
    value_return = funct_welfare.funct_welfare("health", animal, farmId, animalNum, timeFrom, timeTo)
    
    return value_return

@welfare_bp.route('/welfare/feeding')
def wf_feeding():
    '''
    Search and return data range for FEEDING score of an animal.
    
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
    #Check values we need
    #Values are required: animal, farmId, *animalId
    value_return = funct_welfare.funct_welfare("feeding", animal, farmId, animalNum, timeFrom, timeTo)
    
    return value_return


@welfare_bp.route('/welfare/housing')
def wf_housing():
    '''
    Search and return data range for HOUSING score of an animal.
    
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
    #Check values we need
    #Values are required: animal, farmId, *animalId
    value_return = funct_welfare.funct_welfare("housing", animal, farmId, animalNum, timeFrom, timeTo)
    
    return value_return
    
@welfare_bp.route('/welfare/global')
def wf_global():
    '''
    Search and return data range for GLOBAL score of an animal.
    
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
    #Check values we need
    #Values are required: animal, farmId, *animalId
    value_return = funct_welfare.funct_welfare("global", animal, farmId, animalNum, timeFrom, timeTo)
    
    return value_return
            
