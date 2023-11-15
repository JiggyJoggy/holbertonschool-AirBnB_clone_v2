#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_states():
    return render_template(
        '8-cities_by_states.html',
        states_list=storage.all('State').values()
    )


@app.teardown_appcontext
def remove(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
