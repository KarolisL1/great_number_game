from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['computer_num'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/process_guess', methods = ['POST'])
def process_guess():
    print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(f'User guess: {request.form["guess"]}')
    print(f"computer guess {session['computer_num']}")

    if int(request.form['guess']) == session['computer_num']:
        session['result'] = "You win!"
    elif int(request.form['guess']) > session['computer_num']:
        session['result'] = "Too high!"
    else:
        session['result'] = "Too low!"

    return redirect('/results')

@app.route('/results')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)