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
    
    return "hola, entraste"

            
