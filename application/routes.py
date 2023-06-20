from flask import render_template, request
from application import app
from application.forms import LoginForm, RecordForm
#from application.summarize import create_summary
from application.summarize_ai import summarize_with_ai
from application.scatterplot import scatterplot
from application.bubbleplot import bubbleplot
from application.mcgill_pain_questionnaire import mcgill_feels_like, mcgill_change, mcgill_increase, Mcgill_intensity
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if request.method == 'POST':
        pain = form.pain.data
        #mchill = form.mchill.data
        symptoms = form.symptoms.data
        now = datetime.now()
        date_time_str = now.strftime("%d-%m-%Y %H:%M")
        with open('./file_output/symptoms.txt', 'a') as f:
            f.write(date_time_str + '<br>' + symptoms + '<br>' + 'Pain=' + str(pain) + '<br>')
        # if mchill == True:
        #     return render_template('mchill_pain_scale.html', title="McHill Pain Scale")
        # else: #(don't forget indent)
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
    summary = summarize_with_ai().choices[0].text
    pain = False
    if pain == False:
        # create symptom scatterplot or bubbleplot to add a dimension of pain information
        scatterplot()
    else:
        bubbleplot()
    return render_template('display_summary.html', title='Symptom Summary', summary=summary, pain=pain)

@app.route('/mcgill', methods=['GET', 'POST'])
def mcgill():
    pain_words = mcgill_feels_like
    return render_template('1_pain_questionnaire.html', title='McGill Pain Questionnaire', pain_words=pain_words)