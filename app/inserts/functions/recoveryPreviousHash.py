from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from datetime import datetime
from werkzeug.utils import secure_filename
import csv
import json
import os

from .. import inserts_bp
from app import UPLOAD_FOLDER

def recoveryPreviousHash(dataBase):
    data = list(dataBase.find({}, {"hash": 1}).sort("$natural", -1))
    
#    if data:
    try:
        dict_aux = data[0]
        dict = {'hash_previous': dict_aux['hash']}
    except:
#    else:
        dict = {'hash_previous': '0'}

    return dict


