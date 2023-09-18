from flask import Blueprint

validate_bp = Blueprint('validate', __name__, template_folder='templates')

from .resources import validate
