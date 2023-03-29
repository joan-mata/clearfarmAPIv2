from flask import Flask

from .. import dbtest_bp


@dbtest_bp.route('/dbtest')
def home():
    '''
    Welcome to dbTest
    
    Args:
        None
    '''
    
    return "Welcome to dbTest."

            
