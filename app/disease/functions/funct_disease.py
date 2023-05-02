from flask import Flask, request

from app import db_cows
from app import msg_dict

from .. import disease_bp
from ..functions import diseaseLastCow
from ..functions import diseaseLastFarm
from ..functions import diseaseRangeCow
from ..functions import diseaseRangeFarm

def funct_disease(disease, animal, farmId, animalNum, timeFrom, timeTo):
    quantity = "Last"
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
            value_return = diseaseLastCow.diseaseLastCow(disease, animalNum)
        else:
            value_return = diseaseRangeCow.diseaseRangeCow(disease, animalNum, timeFrom, timeTo)
    #Search all animals in farm
    else:
        if quantity == "Last":
            value_return = diseaseLastFarm.diseaseLastFarm(disease, farmId)
        else:
            value_return = diseaseRangeFarm.diseaseRangeFarm(disease, farmId, timeFrom, timeTo)
        
    return value_return
