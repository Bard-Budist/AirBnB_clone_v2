#!/usr/bin/python3
"""First Task"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task0():
    """Task 0"""
    return "Hello HBNB!"


app.run(host="0.0.0.0", port=5000)
