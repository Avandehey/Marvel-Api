from flask import render_template

from . import bp
from app import app

@bp.route('/')
def home():
    return render_template('index.jinja')
