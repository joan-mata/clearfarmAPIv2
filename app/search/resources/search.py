from flask import Flask, request

from .. import search_bp
from ..functions import searchAllCow
from ..functions import searchAllFarm
from ..functions import searchLastCow
from ..functions import searchLastFarm
from ..functions import searchRangeCow
from ..functions import searchRangeFarm


@search_bp.route('/search', methods=['GET'])
def search():
    '''
    Search within REST-API.
    
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
        animalId: { def: "identificator for a group of data",
                    type: string,
                    required: "depending (if your insert a 'animalNum', 'animalId' is required",
                    default: 'none',
                    values: "many and variables",
                    comment: "this args have correlation with 'animalNum'."
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: int,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                    comment: "this args have correlation with 'animalId'."
                },
        quantity: { def: "how much information do you want about the animal or farm.",
                    type: string,
                    required: no,
                    default: 'Last',
                    values: ['Last', 'All', 'Range'],
                    comment: "If you insert any value in 'timeFrom', the 'quantity' value are not important, because change automaticaly to 'Range'."
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
    
    Return: {
        error_required_animal: "Is required the 'animal' value.",
        error_required_farmId: "Is required the 'farmId' value.",
        error_value_farmId: "Value is smaller than 1."
        
        error_animalId: "Is required the 'animalId' value because you have inserted the 'animalNum' value.",
        error_format_timeFrom: "Format of 'timeFrom' is not correct.",
        error_format_timeTo: "Format of 'timeTo' is not correct.",
        error_today_timeFrom: "'timeFrom' value is greater than today's date."
        error_today_timeTo: "'timeTo' value is greater than today's date."
        error_small_timeTo: "'timeTo' value is smaller than 'timeFrom' value"

    }
        
    '''
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalId = request.args.get('animalId', default = 'none', type = str)
    animalNum = str(request.args.get('animalNum', default = 0, type = int))
    quantity = request.args.get('quantity', default = 'Last', type = str)
    timeFrom = request.args.get('timeFrom', default = 'none', type = str)
    timeTo = request.args.get('timeTo', default = 'none', type = str)
    
    #TODO: delete
    value = {
            "animal": animal,
            "farmId": farmId,
            "animalId": animalId,
            "animalNum": animalNum,
            "quantity": quantity,
            "timeFrom": timeFrom,
            "timeTo": timeTo,
    }
    
    #Check values we need
    #Values are required: animal, farmId, *animalId
    

    #Check if you have inserted timeFrom
    if timeFrom != 'none':
        quantity = "Range"
    
    #Check values to animal
    if animal == "none":
        value_return = { "type": "error",
                        "name": "error_required_animal",
                        "text": "Is required the 'animal' value.",
                        }
    #Check values to farmId 
    elif int(farmId) <= 0:
        if farmId == "0":
            value_return = {"type": "error",
                            "name": "error_required_farmId",
                            "text": "Is required the 'farmId' value or the value is not a integer.",
                            }
        else:
            value_return =  { "type": "error",
                            "name": "error_value_farmId",
                            "text": "Value is smaller than 1.",
                            }
    #Check if you have inserted animalNum
    elif animalNum != "0":
        #Check values to animalId
        if animalId == "none":
            value_return  = { "type": "error",
                            "name": "error_required_animalId",
                            "text": "Is required the 'animalId' value because you have inserted the 'animalNum' value.",
                            }
        #Search concrete animal
        else:
            if quantity == "Last":
                value_return = searchLastCow.searchLastCow(farmId, animalNum, animalId)
            elif quantity == "All":
                value_return = searchAllCow.searchAllCow(farmId, animalNum, animalId)
            else:
                value_return = searchRangeCow.searchRangeCow(farmId, animalNum, animalId, timeFrom, timeTo)
    #Search all animals in farm
    else:
        if quantity == "Last":
            value_return = searchLastFarm.searchLastFarm(farmId)
        elif quantity == "All":
            value_return = searchAllFarm.searchAllFarm(farmId)
        else:
            value_return = searchRangeFarm.searchRangeFarm(farmId, timeFrom, timeTo)
        
        
    print("DATA " + str(type(value_return)))

    #TODO: Comprove timeFrom format
    #TODO: Comprove timeTo format
    #TODO: Comprove timeFrom < today
    #TODO: Comprove timeTo < today
    #TODO: Comprove timeFrom < timeTo
    
    return value_return

            
