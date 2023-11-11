#!/usr/bin/python3
"""Returning Hello HBNB! & HBNB with using Flask
display "C", followed by the value of the text variable
display "Python", followed by the value of the text variable
The default value of text is “is cool”
"""
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
