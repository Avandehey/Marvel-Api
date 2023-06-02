from flask import Blueprint

bp = Blueprint('marvel' , __name__)

from . import routes