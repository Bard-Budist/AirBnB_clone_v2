#!/usr/bin/python3
"""First Task"""
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', strict_slashes=False)
def task0():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def task1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def task2(text):
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python', strict_slashes=False, defaults={'text': "is cool"})
@app.route('/python/(<text>)', strict_slashes=False)
def task3(text):
    text = text.replace('_', ' ')
    return "Python %s" % escape(text)


@app.route('/number/<int:n>')
def task4(n):
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def task5(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def task6(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
