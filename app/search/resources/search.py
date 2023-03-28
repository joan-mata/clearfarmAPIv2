from flask import Flask, request

from .. import search_bp


@search_bp.route('/search', methods=['GET'])
def search():
    '''
    Presentation to REST-API.
    
    Args: [
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
                    required: yes,
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
                    format date: 'dd/mm/yyyy',
                    default: 'none',
                    values: date,
                    comment: "If you insert any value in 'timeFrom', the 'quantity' value are not important, because change automaticaly to 'Range'."
                },
        timeTo: {   def: "upper limit for the range of dates where we want to search information",
                    type: string,
                    required: no,
                    format date: 'dd/mm/yyyy',
                    default: 'none',
                    values: "any date greater than 'timeFrom' and smaller than today",
                    comment: "If you do not insert any value in 'timeFrom', the 'timeTo' does not work."
                },
    ]
        
    '''
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = request.args.get('farmId', default = 0, type = int)
    animalId = request.args.get('animalId', default = 'none', type = str)
    animalNum = request.args.get('animalNum', default = 0, type = int)
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
    
    
    
    return value

            
