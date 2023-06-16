from wtforms import SubmitField, StringField, BooleanField
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Submit')

class RecordForm(FlaskForm):
    pain = BooleanField('Pain', default=False)
    mchill = BooleanField('Pain Scale', default=False)
    symptoms = StringField('Symptoms')
    submit = SubmitField('Submit')

    
