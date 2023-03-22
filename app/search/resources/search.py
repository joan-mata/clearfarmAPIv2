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
    animalId = request.args.get('animalId', default = 'cowID', type = str)
    quantity = request.args.get('quantity', default = 'last', type = str)
    timeFrom = request.args.get('timeFrom', default = '', type = str)
    timeTo = request.args.get('timeTo', default = '', type = str)

    if timeFrom != "":
            quantity = "Range"
        
        if cowNum == "":
            if quantity == "Last":
                stringHtml, data = searchLastFarm.searchLastFarm(farmID)
            elif quantity == "All":
                stringHtml, data = searchLastFarm.searchLastFarm(farmID)
            else:
                stringHtml, data = searchRangeFarm.searchRangeFarm(farmID, timeFrom, timeTo)
        else:
            if quantity == "Last":
                stringHtml, data = searchLastCow.searchLastCow(farmID, cowNum, id)
            elif quantity == "All":
                stringHtml, data = searchAllCow.searchAllCow(farmID, cowNum, id)
            else:
                stringHtml, data = searchRangeCow.searchRangeCow(farmID, cowNum, id, timeFrom, timeTo)
                
        json_object = data
                    
    return json_object

            
