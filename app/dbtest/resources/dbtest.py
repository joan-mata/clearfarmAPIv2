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
    
    reference_list = list(db_cows["reference"].find())
    
    
    return_value = {
        "db": str(db_cows),
        "reference_list": reference_list[0]
    }
    
    
    
    return return_value

            
