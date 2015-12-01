"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

#BEGIN UNMODULATED CODE
import json
from google.appengine.api import urlfetch

def buildSentReq(text, api_key):
    return 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=' + text + '&apikey=' + api_key
  
def getData(text):
	text = text.replace(" ","+")
	url = buildSentReq(text, '944a963d-b63c-4d65-a562-d9507ca49571')
	result = urlfetch.fetch(url)
	if result.status_code == 200:
		jsonSent = json.loads(result.content)
		score = jsonSent['aggregate']['score']
		answer = jsonSent['aggregate']['sentiment']
		return [score, answer]
#END UNMODULATED CODE

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/sentiment/', methods=['POST'])
def sentiment():
	sentiment_text = request.form['sentiment']
	score, answer = getData(sentiment_text)	#NEEDS TO BE MODULATED
	return render_template('index.html', sentiment = "Text: " + sentiment_text, score = "Score: " + str(score), answer = "Conclusion: " + answer)


@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500
