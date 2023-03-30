from flask import Flask

from app import error_dict

from .. import errors_bp


@errors_bp.route('/errors')
def errors():
    '''
    List of errors
    
    Args:
        None
    '''
    
    
    
    return error_dict

            
