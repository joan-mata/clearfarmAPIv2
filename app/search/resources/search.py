from flask import Flask, request

from .. import search_bp


@search_bp.route('/search', methods=['GET'])
def search():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    animal = request.args.get('animal', default = 'none', type = str)

    return "REST-API search " + str(animal)

            
