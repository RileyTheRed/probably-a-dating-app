import sqlite3 as sql
from flask import Flask, request, render_template
from flask.ext.wtf import Form
from wtforms import BooleanField, PasswordField, SubmitField, TextField
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

class LoginForm(Form):
    user_email = TextField('Email', validators=[InputRequired(), Length(min=4, max=15)])
    user_pass = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])

class SignupForm(Form):
    first_name = TextField('First Name', validators=[InputRequired(), Length(min=4, max=15)])
    last_name = TextField('Last Name', validators=[InputRequired(), Length(min=4, max=15)])
    user_email = TextField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    user_pass = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=15)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    form = SignupForm()
    
    return render_template('signup.html', questions=questions)

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
