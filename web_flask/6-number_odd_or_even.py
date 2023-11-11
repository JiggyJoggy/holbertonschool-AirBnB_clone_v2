#!/usr/bin/python3
"""Returning Hello HBNB! & HBNB with using Flask
display "C", followed by the value of the text variable
display "Python", followed by the value of the text variable
The default value of text is “is cool”
display “n is a number” only if n is an integer
display a HTML page only if n is an integer
even or odd"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_(text):
    return f'C {text.replace("_", " ")}'


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_(text=None):
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        num_odd_even = 'even'
    else:
        num_odd_even = 'odd'
    return render_template('6-number_odd_or_even.html', number=n,
                           num_odd_even=num_odd_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
