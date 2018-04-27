import sqlite3 as sql
from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField, SelectField, RadioField, HiddenField
from flask_mail import Mail, Message
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

#Flask-Mail:
#Configuring the email server and authentication for the contact form
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'developmentConfig@gmail.com'
app.config['MAIL_PASSWORD'] = '@config123456'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

sender = 'developmentConfig@gmail.com'
 
def send_email(subject, sender, recipients, text_body):
    with app.app_context():
        msg = Message(subject, sender=sender, recipients=[recipients])
        msg.body = text_body
        mail.send(msg)

#send_email('hello', sender, ['dlaesker@mail.usf.edu'], 'hello')
        
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
    msg = 'All options must be selected!'
    q_one = RadioField(questions[0]['1'], choices=L, validators=[InputRequired(message=msg)])
    q_two = RadioField(questions[1]['2'], choices=L, validators=[InputRequired(message=msg)])
    q_three = RadioField(questions[2]['3'], choices=L, validators=[InputRequired(message=msg)])
    q_four = RadioField(questions[3]['4'], choices=L, validators=[InputRequired(message=msg)])
    q_five = RadioField(questions[4]['5'], choices=L, validators=[InputRequired(message=msg)])
    q_six = RadioField(questions[5]['6'], choices=L, validators=[InputRequired(message=msg)])
    q_seven = RadioField(questions[6]['7'], choices=L, validators=[InputRequired(message=msg)])
    q_eight = RadioField(questions[7]['8'], choices=L, validators=[InputRequired(message=msg)])
    q_nine = RadioField(questions[8]['9'], choices=L, validators=[InputRequired(message=msg)])
    q_ten = RadioField(questions[9]['10'], choices=L, validators=[InputRequired(message=msg)])
    
class ContactForm(FlaskForm):
    name = TextField('Name', validators=[InputRequired(message='Name required!')],              render_kw={"placeholder": "Enter name"})
    email = TextField('Email', validators=[InputRequired(message="You must enter an             email!"), Email(message='Invalid email'), Length(max=50)], render_kw=               {"placeholder": "Enter email"})
    subject = SelectField('Subject', validators=[InputRequired(message="error")], choices=[('General Customer Service', 'General Customer Service'),                 ('Suggestions', 'Suggestions')])
    message = TextField('Message', validators=[InputRequired(message=''), Length(min=4,           max=15)], render_kw={"placeholder": "Enter your message here"})
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #if login information in database -> return 'dashboard'
    if form.validate_on_submit():
        return form.user_email.data
    return render_template('login.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contactform = ContactForm()
    if contactform.validate_on_submit():
        send_email('Coffee and Bagels', sender, contactform.email.data, 'We received your email!')
        send_email(contactform.subject.data, sender, sender, contactform.message.data)
    return render_template('contact.html', contactform=contactform)



#################
#LOOK HERE RILEY#
#################
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    Q = Questionnaire()
    #You can access the data by doing 'form.<member variable>.data'
    #member variables: look in the SignupForm class
    #return dashboard(L)
    
    if form.validate_on_submit() and Q.validate_on_submit():
        #return form.first_name.data
        return Q.q_one.data
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
def dashboard(user_name=None, comp=None, mutual_likes=None):
    return render_template('dashboard.html')

@app.route('/profile')
def profile(user_info=None):
    return render_template('profile.html', user_info=user_info)

if __name__ == "__main__":
    app.run(debug=True)
