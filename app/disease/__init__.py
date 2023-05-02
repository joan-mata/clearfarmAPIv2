from flask import Blueprint

disease_bp = Blueprint('disease', __name__, template_folder='templates')

from .resources import disease
