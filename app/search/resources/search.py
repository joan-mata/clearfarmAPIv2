from flask import Flask, render_template, request, url_for, redirect, session, send_file, send_from_directory
from bson import json_util

import json
import pandas as pd

from .. import search_bp


@search_bp.route('/search', methods=['GET'])
def search():
    '''
    Treath the answers of Cow Form
    
    Args:
        None
    '''
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = request.args.get('farmId', default = 0, type = int)
    animalId = args.get('animalId', default = 'cowID', type = str)
    quantity = args.get('quantity', default = 'last', type = str)
    timeFrom = args.get('timeFrom', default = '', type = str)
    timeTo = args.get('timeTo', default = '', type = str)

    json_object = {"animal": animal}
                    
    return "works"

            
