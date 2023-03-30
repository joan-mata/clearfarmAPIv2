from flask import Flask

from .. import insert_bp


@insert_bp.route('/insert')
def insert():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."

            
