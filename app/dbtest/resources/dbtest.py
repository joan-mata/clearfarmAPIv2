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
    
    
    return_value = {
        "db": str(db_cows),
        "reference_list": str(reference_list[0]),
        "referenceIds": str(referenceIds)
    }
    
    
    
    return return_value

            
