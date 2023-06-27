from wtforms import SubmitField, StringField, RadioField, SelectMultipleField
from flask_wtf import FlaskForm
from application.mcgill_pain_questionnaire import mcgill_feels_like

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Submit')

class RecordForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    pain = RadioField('Pain', choices=[('True', 'I am in pain'), ('False', 'No pain')])
    mcgill = RadioField('McGill', choices=[('True', 'I want to record my pain'), ('False', 'skip this step')])
    symptoms = StringField('Symptoms')
    submit = SubmitField('Submit')

class McgillForm(FlaskForm):
    # be careful with this because you want to be able to access the words for the wordweb
    adjectives1 = SelectMultipleField('adjectives1', choices=[(1, 'flickering'), (2, 'quivering'), (3, 'pulsing'), (4, 'throbbing'), (5, 'beating'), (6, 'pounding')])
    adjectives2 = SelectMultipleField('adjectives2', choices=[(1, 'jumping'), (2, 'flashing'), (3, 'shooting')])
    adjectives3 = SelectMultipleField('adjectives3', choices=[(1, 'pricking'), (2, 'boring'), (3, 'drilling'), (4, 'stabbing'), (5, 'lancinating')])
    adjectives4 = SelectMultipleField('adjectives4', choices=[(1, 'sharp'), (2, 'cutting'), (3, 'lacerating')])
    adjectives5 = SelectMultipleField('adjectives5', choices=[(1, 'pinching'), (2, 'pressing'), (3, 'gnawing'), (4, 'cramping'), (5, 'crushing')])
    adjectives6 = SelectMultipleField('adjectives6', choices=[(1, 'tugging'), (2, 'pulling'), (3, 'wrenching')])
    adjectives7 = SelectMultipleField('adjectives7', choices=[(1, 'hot'), (2, 'boring'), (3, 'scalding'), (4, 'searing')])
    adjectives8 = SelectMultipleField('adjectives8', choices=[(1, 'tingling'), (2, 'itchy'), (3, 'smarting'), (4, 'stinging')])
    adjectives9 = SelectMultipleField('adjectives9', choices=[(1, 'dull'), (2, 'sore'), (3, 'hurting'), (4, 'aching'), (5, 'heavy')])
    adjectives10 = SelectMultipleField('adjectives10', choices=[(1, 'tender'), (2, 'taut'), (3, 'rasping'), (4, 'splitting')])
    adjectives11 = SelectMultipleField('adjectives11', choices=[(1, 'tiring'), (2, 'exhausting')])
    adjectives12 = SelectMultipleField('adjectives12', choices=[(1, 'sickening'), (2, 'suffocating')])
    adjectives13 = SelectMultipleField('adjectives13', choices=[(1, 'fearful'), (2, 'frightful'), (3, 'terrifying')])
    adjectives14 = SelectMultipleField('adjectives14', choices=[(1, 'punishing'), (2, 'gruelling'), (3, 'cruel'), (4, 'vicious'), (5, 'killing')])
    adjectives15 = SelectMultipleField('adjectives15', choices=[(1, 'wretched'), (2, 'blinding')])
    adjectives16 = SelectMultipleField('adjectives16', choices=[(1, 'annoying'), (2, 'troubling'), (3, 'miserable'), (4, 'intense'), (5, 'unbearable')])
    adjectives17 = SelectMultipleField('adjectives17', choices=[(1, 'spreading'), (2, 'radiating'), (3, 'penetrating'), (4, 'piercing')])
    adjectives18 = SelectMultipleField('adjectives18', choices=[(1, 'tight'), (2, 'numb'), (3, 'drawing'), (4, 'squeezing'), (5, 'tearing')])
    adjectives19 = SelectMultipleField('adjectives19', choices=[(1, 'cool'), (2, 'cold'), (3, 'freezing')])
    adjectives20 = SelectMultipleField('adjectives20', choices=[(1, 'nagging'), (2, 'nauseating'), (3, 'agonizing'), (4, 'dreadful'), (5, 'torturing')])
    
    change = SelectMultipleField('change', choices=[(1, 'continous steady constant'), (2, 'rhythmic periodic intermittent'), (3, 'brief momentary transient')])
    increase = SelectMultipleField('increase', choices=[(1, 'liquor'), (2, 'stimulants'), (3, 'eating'), (4, 'heat'), (5, 'cold'), (6, 'damp'), (7, 'weather changes'), (8, 'massage or use of a vibrator'), (9, 'pressure'), (10, 'no movement'), (11, 'movement'), (12, 'sleep'), (13, 'lying down'), (14, 'distraction (TV, reading etc)'), (15, 'urination or defecation'), (16, 'tension'), (17, 'bright lights'), (18, 'loud_noises'), (19, 'going to work'), (20, 'intercourse'), (21, 'mild exercise'), (22, 'fatigue')], default=False)
    intensity = RadioField('Intensity', choices=[('0', 'No Pain'), ('1', 'Mild'), ('2', 'Discomforting'), ('3', 'Distressing'), ('4', 'Horrible'), ('5', 'Excruciating')])
    
    submit = SubmitField('Submit')

