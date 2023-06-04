from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import UserMixin
from datetime import datetime

from app import db, login , uuid

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin , db.Model):
    user_id = db.Column(db.String(36), primary_key=True , default=uuid)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    marvel = db.relationship('Marvel' , backref='author' , lazy=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commmit()

    def hash_password(self, password):
        return generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.user_id)
    
class Marvel(db.Model):
    id = db.Column(db.String(36), primary_key=True , default=uuid)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    comics_appeared_in = db.Column(db.String(250))
    super_power = db.Column(db.String(50))
    date_created = db.Column(db.DateTime , default = datetime.utcnow())
    owner = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return f'Hero: {self.name}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()