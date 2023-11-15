#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_(id):
    req = None
    states_list = storage.all('State').values()
    if id is not None:
        req = next(
            (state for state in states_list if state.id == id),
            False
        )
    return render_template(
        '9-states.html',
        req=req,
        states_list=states_list
    )


@app.teardown_appcontext
def remove(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
