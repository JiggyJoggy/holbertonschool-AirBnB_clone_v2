#!/usr/bin/python3
"""Returning Hello HBNB! & HBNB with using Flask"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB_route():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
