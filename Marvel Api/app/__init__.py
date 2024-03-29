from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import uuid


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
uuid = str(uuid.uuid4())

login.login_view = 'auth.signin'

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.marvel import bp as marvel_bp
app.register_blueprint(marvel_bp)
from app.blueprints.api import bp as api_bp
app.register_blueprint(api_bp)

from app import models