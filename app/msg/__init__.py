from flask import Blueprint

msg_bp = Blueprint('msg', __name__, template_folder='templates')

from .resources import msg
