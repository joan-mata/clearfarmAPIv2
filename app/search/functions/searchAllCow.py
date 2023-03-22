from flask import Flask, render_template, request, url_for, redirect, session, send_file, send_from_directory
from bson import json_util

import csv
import json
import pandas as pd

from .. import search_bp
from app import db_cows

# Flask Searches Cow
def searchAllCow(farmID, cowNum, id):
    '''
    Search ALL information about ONE cow
    
    Args:
        None
    '''
    #find id's in reference collection
    referenceIds = list(db_cows["reference"].find({"$and":[{"farmID": farmID},{id: cowNum}]}).sort("$natural", -1))
        
    if referenceIds:
        referenceIds = referenceIds[0]
    else:
        return 'prints/printErrorReference.html', "No information about the cow in this farm"
        
    #recovery collections - id matrix (list of dictionarys)
    matrix = list(db_cows["listCollections"].find({"collection": {"$exists": "true"}}))

    data = []
    for item in matrix: #each item is a dictionary
        #item values
        itemCollection = item["collection"]
        itemId = item["key"]

        #referenceIds values
        referenceFarmId = referenceIds["farmID"]
        referenceCowNum = referenceIds[itemId]
        
        temporalData = list(db_cows[itemCollection].find({"$and":[{"farmID": referenceFarmId},{itemId: referenceCowNum}]}).sort("$natural", -1))
        if temporalData:
            data.append(temporalData)
            
    if data:
        html = 'prints/printAllCow.html'
    else:
        html = 'prints/printCowEmpty.html'

    return html, data
