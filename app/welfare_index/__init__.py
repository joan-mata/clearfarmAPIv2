from flask import Blueprint

welfare_index_bp = Blueprint('welfare_index', __name__, template_folder='templates')

from .resources import welfare_index