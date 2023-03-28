from flask import Flask

from .. import search_bp


@search_bp.route('/search')
def search():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    
    return "REST-API search"

            
