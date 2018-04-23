import sqlite3 as sql
from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField, SelectField, RadioField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo, Length
from wtforms import ValidationError

questions = [{"1":"When I make a plan, I stick to it."},{"2":"I take time out of my day for others."},
    {"3":"I feel unable to deal with things."},{"4":"I love to help others."},{"5":"I seek adventure."},
    {"6":"The first place I put my dirty clothes is in the hamper."},{"7":"I often carry the conversation to a higher level."},
    {"8":"I am a morning peson."},{"9":"I other make others feel good."},{"10":"I am good at analyzing problems."},
    {"11":"I usually stand up for myself."},{"12":"I am easily discouraged."},{"13":"I can handle a lot of information."},
    {"14":"Communication is very important in a relationship."},
    {"15":"Being honest about a tough issue is better than lying about it to avoid the topic."},
    {"16":"Reliability is an honorable trait in a person."},{"17":"I am patient about things out of my control."},
    {"18":"Sexual chemistry is very important in a relationship."},{"19":"If you are in a relationship it is still okay to flirt with other people."},
    {"20":"I believe in true love."}]

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SOMETHINGGOESHERE'

class LoginForm(FlaskForm):
    user_email = TextField('Email Address', validators=[InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "Email Address"})
    user_pass = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": "Password"})

class SignupForm(FlaskForm):
    first_name = TextField('First Name', validators=[InputRequired(message='Enter a First Name!'), Length(min=4, max=15)], render_kw={"placeholder": "First Name"})
    last_name = TextField('Last Name', validators=[InputRequired(message='Enter a Last Name!'), Length(min=4, max=15)], render_kw={"placeholder": "Last Name"})
    user_email = TextField('Email', validators=[InputRequired(message="You must enter an email!"), Email(message='Invalid email'), Length(max=50)], render_kw={"placeholder": "Email"})
    user_pass = PasswordField('Password', validators=[InputRequired(message='You must enter a password!'), Length(min=4, max=15)], render_kw={"placeholder": "Password"})
    user_gender = SelectField('What is your gender?', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    user_want_gender = SelectField('Who are you looking to be matched with?', choices=[ ('female', 'Female'), ('male', 'Male'), ('no_preference', 'No preference')])
    take_coffee = SelectField('How do you take your coffee?', choices=[('black', 'Black'), ('wcream', 'With Cream'), ('wmilk', 'With Milk')])

class Questionnaire(FlaskForm):
    L = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    q_one = RadioField(questions[0]['1'], choices=L)
    q_two = RadioField(questions[1]['2'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_three = RadioField(questions[2]['3'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_four = RadioField(questions[3]['4'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_five = RadioField(questions[4]['5'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_six = RadioField(questions[5]['6'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_seven = RadioField(questions[6]['7'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_eight = RadioField(questions[7]['8'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_nine = RadioField(questions[8]['9'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    q_ten = RadioField(questions[9]['10'], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    
#class ContactForm(FlaskForm):
#    name = 
#    email = 
#    subject = 
#    message = 
#    send = 
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #if login information in database -> return 'dashboard'
    return render_template('login.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    Q = Questionnaire()
    if form.validate_on_submit():
        return form.first_name.data
    #if user not yet in database -> register
    
    #else -> print error message
    return render_template('signup.html', questions=questions, form=form, Q=Q)

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = SignupForm(request.form)
#     if request.method == 'POST' and form.validate():
#         # user = User(form.username.data, form.email.data,
#         #             form.password.data)
#         # db_session.add(user)
#         flash('Thanks for registering')
#         return redirect(url_for('login'))
#     return render_template('signup.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
