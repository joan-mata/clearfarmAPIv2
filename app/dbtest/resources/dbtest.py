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
    
    return_value = {
        "db": db_cows
    }
    
    
    
    return return_value

            
