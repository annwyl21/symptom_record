from flask import render_template, request
from application import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == 'password':
            return render_template('record.html')
    return render_template('login.html')

@app.route('/record', methods=['POST'])
def record():
        if request.method == 'POST':
        symptoms = request.form['username']
        if symptoms:
            return render_template('success.html')
    return render_template('record.html')
