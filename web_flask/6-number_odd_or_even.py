#!/usr/bin/python3
"""Pass multiple params in html."""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Handle '/' route."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Handle '/hbnb' route."""
    return "HBNB"


@app.route('/c/<string:text>')
def handle_params(text):
    """Handle parameters passed in the URL."""
    text = text.replace("_", " ")
    return "c {}".format(text)


@app.route('/python/<string:text>')
@app.route('/python', defaults={'text': 'is cool'})
def handle_defaults(text):
    """Put a default value if params are not passed."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def handle_int(n):
    """Handle route only if the param is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def render_html(n):
    """Pass param in html."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def mult_params(n):
    """Pass multiple param in html."""
    odd_or_even = "even"
    if n % 2 != 0:
        odd_or_even = "odd"
    file_name = '6-number_odd_or_even.html'
    return render_template(file_name, n=n, odd_or_even=odd_or_even)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
