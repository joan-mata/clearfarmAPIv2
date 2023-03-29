from flask import Blueprint

errors_bp = Blueprint('errors', __name__, template_folder='templates')

from .resources import errors
