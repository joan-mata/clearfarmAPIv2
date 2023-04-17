from flask import Flask, request

from app import db_cows
from app import msg_dict

from .. import welfare_bp
from ..functions import welfareLastCow
from ..functions import welfareLastFarm
from ..functions import welfareRangeCow
from ..functions import welfareRangeFarm

@welfare_bp.route('/welfare/health')
def wf_health():
    '''
    Search and return data range for health score of an animal.
    
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
        s
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
    quantity = "Last"
    #Check values we need
    #Values are required: animal, farmId, *animalId

    #Check if you have inserted timeFrom
    if timeFrom != 'none':
        quantity = "Range"
    
    #Check values to animal
    if animal == "none":
        value_return = msg_dict["error_required_animal"]
    #Check values to farmId
    elif int(farmId) <= 0:
        if farmId == "0":
            value_return = msg_dict["error_required_farmId"]
        else:
            value_return = msg_dict["error_value_farmId"]
    #Check if you have inserted animalNum
    elif animalNum != "0":
        #Search concrete animal
        if quantity == "Last":
            value_return = welfareLastCow.welfareLastCow(farmId, animalNum, animalId)
        else:
            value_return = welfareRangeCow.welfareRangeCow(farmId, animalNum, animalId, timeFrom, timeTo)
    #Search all animals in farm
    else:
        if quantity == "Last":
            value_return = welfareLastFarm.welfareLastFarm(farmId)
        else:
            value_return = welfareRangeFarm.welfareRangeFarm(farmId, timeFrom, timeTo)
            
    #TODO: Comprobar si devuelve un diccionario o se ha de hacer una lista por narices
        
    return value_return

@welfare_bp.route('/welfare/feeding')
def wf_feeding():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."


@welfare_bp.route('/welfare/housing')
def wf_housing():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."
    
@welfare_bp.route('/welfare/global')
def wf_global():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."
            
