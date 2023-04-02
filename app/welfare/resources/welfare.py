from flask import Flask

from app import db_cows

from .. import welfare_bp


@welfare_bp.route('/welfare/health')
def wf_health():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    data = db_cows["walfare"].find({"health_score": {"$exists": "true"}})
    
    
    return "Welcome to Clearfarm's REST-API."

@welfare_bp.route('/welfare/feeding')
def wf_feeding():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."


@welfare_bp.route('/welfare/housing')
def wf_housing():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."
    
@welfare_bp.route('/welfare/global')
def wf_global():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "Welcome to Clearfarm's REST-API."
            
