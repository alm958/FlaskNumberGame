from flask import Flask, request, render_template, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'mykey'

@app.route('/', methods=['get','post'])
def count():
    message = None
    error = None
    session['guess_count'] = 0
    session['number']= random.randint(1,100)
    return render_template('index.html', message = message)

@app.route('/guess', methods=['post'])
def guess():
    try:
        val = int(request.form['guess'])
    except ValueError:
        error = "That's not an integer! Enter an integer between 1 and 100."
        return render_template('index.html', error = error)
    session['guess_count'] += 1
    if int(request.form['guess']) > session['number']:
        message = 'Too high. Enter a smaller number. Your guess count so far is '
        return render_template('index.html', message = message)
    elif int(request.form['guess']) < session['number']:
        message = 'Too low. Enter a larger number. Your guess count so far is '
        return render_template('index.html', message = message)
    elif int(request.form['guess']) == session['number']:
        message = 'Correct! Congratulations! Your total guesses was '
        return render_template('index.html', message = message)

@app.route('/reset', methods=['post'])
def reset():
    message = None
    error = None
    session['guess_count'] = 0
    session['number'] = random.randint(1,100)
    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run(debug=True)
