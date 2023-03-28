from flask import Flask

from .. import search_bp


@search_bp.route('/search', methods=['GET'])
def search():
    '''
    Presentation to REST-API.
    
    Args:
        None
    '''
    animal = "hola"
#    animal = request.args.get('animal', default = 'none', type = str)

    return "REST-API search" + str(animal)

            
