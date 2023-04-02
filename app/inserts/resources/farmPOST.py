from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from datetime import datetime
from werkzeug.utils import secure_filename
import csv
import json
import os

from .. import inserts_bp
from app import db, UPLOAD_FOLDER
from ..functions import computeHash
from ..functions import recoveryPreviousHash

@inserts_bp.route('/farmPOST', methods=('GET', 'POST'))
def farmPOST():
    '''
    Insert farm's data in DB
    
    Args:
        None
    '''
    
    if request.method=='POST':
        enterprise = request.form["collections"]

        f = request.files['csvfile']
        filename = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, enterprise + '.csv'))
        
        csvFilePath = r'data/' + enterprise + '.csv'
        
        try: # If exist this enterprise
            count = db['listCollections'].count_documents({"collection": enterprise})
        except: # If not exist this enterprise
            count = 0
            
        if count == 0:
            if enterprise != "reference" and enterprise != "matComp":
                key = request.form["keys"]
                db['listCollections'].insert({"collection": enterprise, "key": key})
                
        data = []
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            #add date from today
            date = datetime.today().strftime('%Y-%m-%d')
            dict = {'date_insert_in_db': date}
            #hashPrevious = recoveryPreviousHash.recoveryPreviousHash(db[enterprise])
            hashPrevious = {'hash_previous': '0'} #DELETE

            for rows in csvReader:
                key = {}
                key.update(dict)
                key.update(hashPrevious)
                key.update(rows)
                hash = computeHash.computeHash(key)
                hashPrevious = hash
                key.update(hash)
                data.append(key)

        db[enterprise].insert_many(data)
        return redirect(url_for('home.home'))

    return render_template('inserts/farmPOST.html')

