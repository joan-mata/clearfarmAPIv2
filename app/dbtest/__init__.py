from flask import Blueprint

dbtest_bp = Blueprint('dbtest', __name__, template_folder='templates')

from .resources import dbtest
