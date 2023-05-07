from flask import Flask, request

from app import db_cows
from app import msg_dict

from .. import disease_bp
from ..functions import diseaseLastCow
from ..functions import diseaseLastFarm
#from ..functions import diseaseRangeCow
#from ..functions import diseaseRangeFarm

def funct_disease(disease, animal, farmId, animalNum):
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
    elif animalNum != "none":
        value_return = diseaseLastCow.diseaseLastCow(disease, animalNum)
    else:
        value_return = diseaseLastFarm.diseaseLastFarm(disease, farmId)
        
    return value_return
