from wtforms import SubmitField, StringField, BooleanField, RadioField
from flask_wtf import FlaskForm
from application.mcgill_pain_questionnaire import mcgill_feels_like

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Submit')

class RecordForm(FlaskForm):
    pain = BooleanField('Pain', default=False)
    mchill = BooleanField('Pain Scale', default=False)
    symptoms = StringField('Symptoms')
    submit = SubmitField('Submit')

class Mcgill1Form(FlaskForm):
    for key, list_of_words in mcgill_feels_like.items():
        for word in list_of_words:
            word = BooleanField(word, default=False)

    # #1
    # flickering = BooleanField('Flickering', default=False)
    # quivering = BooleanField('Quivering', default=False)
    # pulsing = BooleanField('Pulsing', default=False)
    # throbbing = BooleanField('Throbbing', default=False)
    # beating = BooleanField('Beating', default=False)
    # pounding = BooleanField('Pounding', default=False)
    # #2
    # jumping = BooleanField('Jumping', default=False)
    # flashing = BooleanField('Flashing', default=False)
    # shooting = BooleanField('Shooting', default=False)
    # #3
    # pricking = BooleanField('Pricking', default=False)
    # boring = BooleanField('Boring', default=False)
    # drilling = BooleanField('Drilling', default=False)
    # stabbing = BooleanField('Stabbing', default=False)
    # lancinating = BooleanField('Lancinating', default=False)
    # #4
    # sharp = BooleanField('Sharp', default=False)
    # cutting = BooleanField('Cutting', default=False)
    # lacerating = BooleanField('Lacerating', default=False)
    # #5
    # pinching = BooleanField('Pinching', default=False)
    # pressing = BooleanField('Pressing', default=False)
    # gnawing = BooleanField('Gnawing', default=False)
    # cramping = BooleanField('Cramping', default=False)
    # crushing = BooleanField('Crushing', default=False)
    # #6
    # tugging = BooleanField('Tugging', default=False)
    # pulling = BooleanField('Pulling', default=False)
    # wrenching = BooleanField('Wrenching', default=False)
    # #7
    # hot = BooleanField('Hot', default=False)
    # boring = BooleanField('Boring', default=False)
    # scalding = BooleanField('Scalding', default=False)
    # searing = BooleanField('Searing', default=False)
    # #8
    # tingling = BooleanField('Tingling', default=False)
    # itchy = BooleanField('Itchy', default=False)
    # smarting = BooleanField('Smarting', default=False)
    # stinging = BooleanField('Stinging', default=False)
    # #9
    # dull = BooleanField('Dull', default=False)
    # sore = BooleanField('Sore', default=False)
    # hurting = BooleanField('Hurting', default=False)
    # aching = BooleanField('Aching', default=False)
    # heavy = BooleanField('Heavy', default=False)
    # #10
    # tender = BooleanField('Tender', default=False)
    # taut = BooleanField('Taut', default=False)
    # rasping = BooleanField('Rasping', default=False)
    # splitting = BooleanField('Splitting', default=False)
    # #11
    # tiring = BooleanField('Tiring', default=False)
    # exhausting = BooleanField('Exhausting', default=False)
    # #12
    # sickening = BooleanField('Sickening', default=False)
    # suffocating = BooleanField('Suffocating', default=False)
    # #13
    # fearful = BooleanField('Fearful', default=False)
    # frightful = BooleanField('Frightful', default=False)
    # terrifying = BooleanField('Terrifying', default=False)
    # #14
    # punishing = BooleanField('Punishing', default=False)
    # gruelling = BooleanField('Gruelling', default=False)
    # cruel = BooleanField('Cruel', default=False)
    # vicious = BooleanField('Vicious', default=False)
    # killing = BooleanField('Killing', default=False)
    # #15
    # wretched = BooleanField('Wretched', default=False)
    # blinding = BooleanField('Blinding', default=False)
    # #16
    # annoying = BooleanField('Annoying', default=False)
    # troubling = BooleanField('Troubling', default=False)
    # miserable = BooleanField('Miserable', default=False)
    # intense = BooleanField('Intense', default=False)
    # unbearable = BooleanField('Unbearable', default=False)
    # #17
    # spreading = BooleanField('Spreading', default=False)
    # radiating = BooleanField('Radiating', default=False)
    # penetrating = BooleanField('Penetrating', default=False)
    # piercing = BooleanField('Piercing', default=False)
    # #18
    # tight = BooleanField('Tight', default=False)
    # numb = BooleanField('Numb', default=False)
    # drawing = BooleanField('Drawing', default=False)
    # squeezing = BooleanField('Squeezing', default=False)
    # tearing = BooleanField('Tearing', default=False)
    # #19
    # cool = BooleanField('Cool', default=False)
    # cold = BooleanField('Cold', default=False)
    # freezing = BooleanField('Freezing', default=False)
    # #20
    # nagging = BooleanField('Nagging', default=False)
    # nauseating = BooleanField('Nauseating', default=False)
    # agonizing = BooleanField('Agonizing', default=False)
    # dreadful = BooleanField('Dreadful', default=False)
    # torturing = BooleanField('Torturing', default=False)

    submit = SubmitField('Submit')
    
class Mcgill2Form(FlaskForm):
    #change
    continous = BooleanField('continous steady constant', default=False)
    periodic = BooleanField('rhythmic periodic intermittent', default=False)
    momentary = BooleanField('brief momentary transient', default=False)
    #increase
    liquor = BooleanField('liquor', default=False)
    stimulants = BooleanField('stimulants such as coffee', default=False)
    eating = BooleanField('eating', default=False)
    heat = BooleanField('heat', default=False)
    cold = BooleanField('cold', default=False)
    damp = BooleanField('damp', default=False)
    weather = BooleanField('weather changes', default=False)
    massage = BooleanField('massage or use of a vibrator', default=False)
    pressure = BooleanField('pressure', default=False)
    no_movement = BooleanField('no movement', default=False)
    movement = BooleanField('movement', default=False)
    sleep = BooleanField('sleep or rest', default=False)
    lying_down = BooleanField('lying down', default=False)
    distraction = BooleanField('distraction (TV, reading etc)', default=False)
    urination = BooleanField('urination or defecation', default=False)
    tension = BooleanField('tension', default=False)
    bright_lights = BooleanField('bright lights', default=False)
    loud_noises = BooleanField('loud noises', default=False)
    going_to_work = BooleanField('going to work', default=False)
    intercourse = BooleanField('intercourse', default=False)
    mild_exercise = BooleanField('mild exercise', default=False)
    fatigue = BooleanField('fatigue', default=False)

    submit = SubmitField('Submit')

class Mcgill3Form(FlaskForm):
    intensity = RadioField('Intensity', choices=[('0', 'No Pain'), ('1', 'Mild'), ('2', 'Discomforting'), ('3', 'Distressing'), ('4', 'Horrible'), ('5', 'Excruciating')])
    submit = SubmitField('Submit')

