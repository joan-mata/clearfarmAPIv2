from flask import Flask, request

from app import db_cows
from app import msg_dict

from .. import welfare_bp
from ..functions import welfareLastCow
from ..functions import welfareLastFarm
from ..functions import welfareRangeCow
from ..functions import welfareRangeFarm

def funct_welfare(welfare, animal, farmId, animalNum, timeFrom, timeTo):
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
            value_return = welfareLastCow.welfareLastCow(welfare, animalNum)
        else:
            value_return = welfareRangeCow.welfareRangeCow(welfare, animalNum, timeFrom, timeTo)
    #Search all animals in farm
    else:
        if quantity == "Last":
            value_return = welfareLastFarm.welfareLastFarm(welfare, farmId)
        else:
            value_return = welfareRangeFarm.welfareRangeFarm(welfare, farmId, timeFrom, timeTo)
        
    return value_return
