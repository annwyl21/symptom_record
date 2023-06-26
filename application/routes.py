from flask import render_template, request
from application import app
from application.database_use import Symptom_log
from application.forms import LoginForm, RecordForm, McgillForm
#from application.summarize import create_summary
from application.summarize_ai import summarize_with_ai
from application.scatterplot import scatterplot
from application.bubbleplot import bubbleplot
#from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if request.method == 'POST':
        pain = form.pain.data
        mcgill = form.mcgill.data
        symptoms = form.symptoms.data

        # capture symptom record in txt file
        now = datetime.now()
        date_time_str = now.strftime("%d-%m-%Y %H:%M")
        with open('./file_output/symptoms.txt', 'a') as f:
           f.write(date_time_str + '<br>' + symptoms + '<br>' + 'Pain=' + str(pain) + '<br>')

        # capture symptom record in database
        username = form.username.data
        password = form.password.data
        user_id = Symptom_log.check_username_password_exist(username, password)
        if user_id == False:
            error = "Please enter username and password"
        else:
            Symptom_log.add_a_symptom(user_id, symptoms)
        if mcgill == 'True':
            return render_template('record_pain.html', title="Record Pain")
        else: 
            return render_template('success.html', title="Success")
    return render_template('record.html', title="Record Symptoms", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        user_id = Symptom_log.check_username_password_exist(username, password)
        if user_id == False:
            error = "Please enter username and password"
        else:
            return render_template('login_success.html', title="Login Success")
    else:
        return render_template('login.html', title="Log in page", form=form, error=error)

@app.route('/display_record')
def display_record():
    # display the txt file
    with open('./file_output/symptoms.txt', 'r') as f:
        content = f.read()
    
    # display the database results
    
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

@app.route('/mcgill_pain_scale', methods=['GET', 'POST'])
def mcgill_pain_scale():
    pain_score = 0
    form = McgillForm()
    if request.method == 'POST':
        print(form.data)
        pain_dictionary = form.data
        for num in range(19):
            string = 'adjectives' + str(num+1)
            for pain_category, score_list in pain_dictionary.items():
                if pain_category == string:
                    for score in score_list:
                        pain_score += int(score)
                if pain_category == 'change':
                    for score in score_list:
                        pain_score += int(score)
                if pain_category == 'increase':
                    for score in score_list:
                        pain_score += int(score)
                if pain_category == 'intensity':
                    for score in score_list:
                        pain_score += int(score)
        print(pain_score)
        return render_template('success.html', title="Success")
    
    else:
        return render_template('mcgill_pain_scale.html', title='McGill Pain Questionnaire', form=form)
