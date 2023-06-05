from wtforms import SubmitField, StringField
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Login')

class RecordForm(FlaskForm):
    symptoms = StringField('Symptoms')
    submit = SubmitField('Submit')

    
