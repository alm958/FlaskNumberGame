from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'mykey'

@app.route('/', methods=['get','post'])
def count():
    error = None
    session['number']= random.randint(1,100)
    session['number']= 50
    return render_template('index.html')

@app.route('/guess', methods=['post'])
def guess():
    if int(request.form['guess']) > session['number']:
        error = 'Too high. Enter a smaller number.'
        return redirect('/')
    elif int(request.form['guess']) < session['number']:
        error = 'Too low. Enter a larger number.'
        return redirect('/')
    elif int(request.form['guess']) == session['number']:
        error = 'Correct! Congratulations!'
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
