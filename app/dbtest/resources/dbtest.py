from flask import Flask

from app import db_cows

from .. import dbtest_bp


@dbtest_bp.route('/dbtest')
def home():
    '''
    Welcome to dbTest
    
    Args:
        None
    '''
    
    farmID = 155
    id = "cowID"
    cowNum = 43490
    
    reference_list = list(db_cows["reference"].find())
    
    referenceIds = list(db_cows["reference"].find({"$and":[{"farmID": farmID},{id: cowNum}]}).sort("$natural", -1))
    
    newfind = list(db_cows["reference"].find(({},{ "farmID": farmID, "cowID": cowNum})))
    
    
    
    return_value = {
        "db": str(db_cows),
        "farmId": farmID,
        "animalId": id,
        "animalNum": cowNum,
        "reference_list": str(reference_list[0]),
        "referenceIds": str(referenceIds),
        "newfind": str(newfind)
    }
    
    
    
    return return_value

            
