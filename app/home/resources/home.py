from flask import Flask

from .. import home_bp


@home_bp.route('/')
def home():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."

            
