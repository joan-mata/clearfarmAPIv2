from flask import Flask, request

from app import msg_dict

from .. import insert_bp


@insert_bp.route('/insert', methods=['POST'])
def insert():
    '''
    Inserts.
    
    Args:
        None
    '''
    
    value_return = msg_dict["error_no_post"]
    
    if request.method == 'POST':
        
        value_return = msg_dict["ok_insert"]
    
    
    return value_return

            
