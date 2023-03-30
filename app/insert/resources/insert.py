from flask import Flask

from .. import insert_bp


@insert_bp.route('/insert')
def insert():
    '''
    Inserts.
    
    Args:
        None
    '''
    
    return "Welcome to INSERT."

            
