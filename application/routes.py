from flask import render_template, request
from application import app
from application.forms import LoginForm, RecordForm
#import os

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == 'POST':
        password = form.password.data
        if password != 'test':
            error = "Please enter username and password"
        else:
            return render_template('record.html')
    else:
        return render_template('login.html', form=form, error=error)

@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if request.method == 'POST':
        symptoms = form.symptoms.data
        if symptoms:
            return render_template('success.html')
    return render_template('record.html', form=form)

@app.route('/display_record.html')
def display_record():
    return render_template('display_record.html')
