from flask import render_template, request
from application import app
from application.database_use import Symptom_log
from application.forms import LoginForm, RecordForm, McgillForm
#from application.summarize import create_summary
from application.summarize_ai import summarize_with_ai
from application.scatterplot import scatterplot
from application.bubbleplot import bubbleplot
from application.data_format import Data_format
from datetime import datetime

# This is a demonstration app to showcase my skills in Python, Flask, PostgreSQL, HTML, CSS, and JavaScript.
# I do not yet know how to code a secure login system, so I am using a global variable to store the user_id.

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
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M")
        Symptom_log.add_a_symptom(my_user_id, symptoms, date, time)
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
        if user_id == 'False':
            error = "Please enter username and password"
        else:
            global my_user_id # using a global variable to work-around login because I don't know how to do it properly yet
            my_user_id = user_id
            return render_template('login_success.html', title="Login Success")
    else:
        return render_template('login.html', title="Log in page", form=form, error=error)

@app.route('/display_record')
def display_record():
    # display the txt file
    with open('./file_output/symptoms.txt', 'r') as f:
        content = f.read()
    # display the database results using the example user_id=2
    symptom_list = Symptom_log.get_symptoms(my_user_id)
    scatterplot(symptom_list)
    list_of_symptom_data = []
    for symptom in symptom_list:
        symptom_data = []
        symptom_data.append(Data_format.us_to_uk_date_format(symptom[0]))
        symptom_data.append(Data_format.remove_seconds_notation(symptom[1]))
        symptom_data.append(symptom[2])
        list_of_symptom_data.append(symptom_data)
        symptom_data_to_display = reversed(list_of_symptom_data)
    return render_template('display_record.html', title="Symptom Record", content=content, list_of_symptoms=symptom_data_to_display)

@app.route('/display_summary')
def display_summary():
    symptoms_summary = summarize_with_ai().choices[0].text
    Symptom_log.add_a_symptom_summary(symptoms_summary, '2023-01-01', '2023-07-01', my_user_id)
    pain = False
    if pain == False:
        # create symptom scatterplot or bubbleplot to add a dimension of pain information
        scatterplot()
    else:
        bubbleplot()
    return render_template('display_summary.html', title='Symptom Summary', summary=symptoms_summary, pain=pain)

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
