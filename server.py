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

    if int(request.form['guess']) < session['computer_num']:
        session['result'] = "Too low!"
        print("Too low!")
        too_low = True
        # session[too_low] = too_low
    elif int(request.form['guess']) > session['computer_num']:
        session['result'] = "Too high!"
        print("Too high!")
        too_high = True
        # session['too_high'] = too_high
    else:
        session['result'] = "You win!"
        print("You win!")
        is_correct = True
        # session[is_correct] = is_correct

    return redirect('/results')

@app.route('/results')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)