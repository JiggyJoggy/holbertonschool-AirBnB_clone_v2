#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    return render_template(
        '7-states_list.html',
        states_list=storage.all('State').values()
    )


@app.teardown_appcontext
def remove(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
