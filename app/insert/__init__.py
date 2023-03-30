from flask import Blueprint

insert_bp = Blueprint('insert', __name__, template_folder='templates')

from .resources import insert
