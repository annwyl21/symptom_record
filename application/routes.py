from flask import render_template, request
from application import app
from application.forms import LoginForm, RecordForm
from application.summarize import Summarize
import time
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if request.method == 'POST':
        symptoms = form.symptoms.data
        now = datetime.now()
        date_time_str = now.strftime("%d-%m-%Y %H:%M")
        with open('./file_output/symptoms.txt', 'a') as f:
            f.write(date_time_str + '<br>' + symptoms + '<br>')
        return render_template('success.html', title="Success")
    return render_template('record.html', title="Record Symptoms", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == 'POST':
        password = form.password.data
        if password != 'test':
            error = "Please enter username and password"
        else:
            return render_template('login_success.html', title="Login Success")
    else:
        return render_template('login.html', title="Log in page", form=form, error=error)

@app.route('/display_record')
def display_record():
    with open('./file_output/symptoms.txt', 'r') as f:
        content = f.read()
    return render_template('display_record.html', title='Symptom Record', content=content)

@app.route('/display_summary')
def display_summary():
    with open('./file_output/symptoms.txt', 'r') as f:
        record = f.read()
        summary = Summarize.create_summary(record)
    return render_template('display_summary.html', title='Symptom Summary', content=summary)
