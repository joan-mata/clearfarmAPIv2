from flask import Flask

from app import msg_dict

from .. import msg_bp


@msg_bp.route('/msg')
def msg():
    '''
    List of errors
    
    Args:
        None
    '''
    
    
    
    return msg_dict

            
