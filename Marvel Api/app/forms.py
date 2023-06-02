from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired , Email

class RegisterForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired()])
    email = StringField('email' , validators=[DataRequired() , Email()])
    password = PasswordField('password' , validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired()])
    password = PasswordField('password' , validators=[DataRequired()])
    submit = SubmitField('Register')

class MarvelForm(FlaskForm):
    name = StringField('name' , validators=[DataRequired()])
    description = StringField('description' , validators=[DataRequired()])
    comics_appeared_in = StringField('comics_appeared_in' , validators=[DataRequired()])
    super_power = StringField('super_power' , validators=[DataRequired()])
    submit = SubmitField('Publish')