from flask import Blueprint

search_bp = Blueprint('search', __name__, template_folder='templates')

from .resources import search
