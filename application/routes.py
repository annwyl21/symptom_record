from flask import render_template, request
from application import app
from application.forms import LoginForm, RecordForm
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == os.environ.get('symptom_record'):
            return render_template('record.html')
        else:
            error = "Please enter username and password"
    else:
        return render_template('login.html')

@app.route('/record', methods=['GET', 'POST'])
def record():
    error = ""
    form = RecordForm()
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        if symptoms:
            return render_template('success.html')
    return render_template('record.html')

@app.route('/display_record.html')
def display_record():
    return render_template('display_record.html')
