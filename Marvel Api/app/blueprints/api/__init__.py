from flask import Blueprint

bp = Blueprint('api' , __name__, url_prefix='/api')

from app.blueprints.api import routes, auth_routes