from flask import Flask, render_template, request
app = Flask(__name__)

questions = ['When I make a plan, I stick to it:', 'I take time out for others:',
             'I feel unable to deal with things:', 'I love to help others:', 
             'I seek adventure', 'The first place I put my dirty clothes is in the hamper:', 'I often carry the conversation to a higher level:', 'I am a morning person:', 'I often make others feel good:', 'I am good at analyzing problems:' 'I usually stand up for myself:', 'I am easily discouraged:', 'I can handle a lot of information:']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def reg():
    return render_template('registration.html', questions=questions)

@app.route('/home')
def home():
    return render_template('home.html')

    
if __name__ == '__main__':
    app.run(debug=True)