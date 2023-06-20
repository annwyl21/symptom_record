from flask import render_template, request
from application import app
from application.forms import LoginForm, RecordForm, Mcgill1Form, Mcgill2Form, Mcgill3Form
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

pain_score = 0

@app.route('/mcgill1', methods=['GET', 'POST'])
def mcgill1():
    form = Mcgill1Form()
    pain_words = mcgill_feels_like
    return render_template('1_pain_questionnaire.html', title='McGill Pain Questionnaire', form=form, pain_words=pain_words)

@app.route('/mcgill2', methods=['GET', 'POST'])
def mcgill2():
    total_change = 0
    total_increase = 0
    form = Mcgill2Form()
    change = form.change.data
    increase = form.increase.data
    if request.method == 'POST':
        print(form.data)
        for score in change:
            total_change += int(score)
        for score in increase:
            total_increase += int(score)
        pain_score += total_change
        pain_score += total_increase
        
    pain_change = mcgill_change
    pain_increase = mcgill_increase
    return render_template('2_pain_questionnaire.html', title='McGill Pain Questionnaire', form=form, pain_change=pain_change, pain_increase=pain_increase)

@app.route('/mcgill3', methods=['GET', 'POST'])
def mcgill3():
    form = Mcgill3Form()
    if request.method == 'POST':
        intensity = form.intensity.data
        pain_score += intensity
        #print(pain_score)
        # add that score into the database and retrieve to generate bubbleplot, forward to success page
    pain_intensity = Mcgill_intensity
    return render_template('3_pain_questionnaire.html', title='McGill Pain Questionnaire', form=form, pain_intensity=pain_intensity)

            # {% for pain_words_list in pain_intensity.values() %}
            #     {% for intensity_description in pain_words_list %}
            #     <div class="form-check">
            #         <input class="form-check-input" type="checkbox" value="{{ pain_words_list.index(intensity_description) }}" id="{{ intensity_description }}">
            #         <label class="form-check-label" for="{{ intensity_description }}">
            #           {{ intensity_description }}
            #         </label>
            #       </div>
            #     {% endfor %}
            # {% endfor %}