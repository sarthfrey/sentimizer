"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/sentiment/', methods=['POST'])
def sentiment():
	sentiment = request.form['sentiment']
	score = 1
	return render_template('index.html', sentiment = "Text: " + sentiment, score = "Score: " + str(score))


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
