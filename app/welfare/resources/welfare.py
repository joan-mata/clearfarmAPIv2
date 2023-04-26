from flask import Flask, request

from app import db_cows
from app import msg_dict

from .. import welfare_bp
from ..functions import welfareLastCow
from ..functions import welfareLastFarm
from ..functions import welfareRangeCow
from ..functions import welfareRangeFarm

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
            
