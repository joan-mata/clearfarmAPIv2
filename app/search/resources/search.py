from flask import Flask, render_template, request, url_for, redirect, session, send_file, send_from_directory
from bson import json_util

import json
import pandas as pd

from .. import search_bp


@search_bp.route('/search') #, methods=['GET'])
def search():
    '''
    Treath the answers of Cow Form
    
    Args:
        None
    '''
    
    args = request.args
    animal = args.get('animal')
    farmId = args.get('farmId')
    
    json_object  = {"animal": animal,
                    "farmId": farmId}
                    
    return json_object

            
