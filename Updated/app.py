import sqlite3 as sql
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#Create a dictionary for the matches of every user 
#and pass it to the html doc
@app.route('/user_page')
def user_page():
    return render_template('user_page.html')

if __name__ == "__main__":
    app.run(debug=True)
