#!/usr/bin/python3
"""First Task"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close():
    storage.close()

@app.route("/states_list", strict_slashes=False)
def task7():
    return render_template("7-states_list.html", states=storage.all(State))

app.run(host="0.0.0.0", port=5000)