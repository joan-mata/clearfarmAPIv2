from flask import Blueprint

welfare_bp = Blueprint('welfare', __name__, template_folder='templates')

from .resources import welfare
