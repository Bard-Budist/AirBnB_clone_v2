#!/usr/bin/python3
"""First Task"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def task10():
    return render_template(
            "10-hbnb_filters.html",
            state=storage.all(State),
            amenity=storage.all(Amenity))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
