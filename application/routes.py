from flask import render_template, request
from application import app
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == os.environ.get('symptom_record'):
            return render_template('record.html')
    return render_template('login.html')

@app.route('/record', methods=['POST'])
def record():
        if request.method == 'POST':
            symptoms = request.form['symptoms']
            if symptoms:
                with open('symptoms.txt', 'a') as f:
                    f.write(symptoms + '\n')
                return render_template('success.html')
        elif request.method == 'GET':
             return render_template('display_record.html')
    return render_template('record.html')
