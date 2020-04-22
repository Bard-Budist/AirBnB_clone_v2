#!/usr/bin/python3
"""First Task"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def task8():
    return render_template(
            "8-cities_by_states.html",
            state=storage.all(State),
            name_class="States")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
