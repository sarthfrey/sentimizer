# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:18:54 2015

@author: prcobol
"""
import urllib3
import json
#from google.appengine.api import urlfetch
#from havenondemand.hodindex import HODClient



def buildSentReq(text, api_key):
    return 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=' + text + '&apikey=' + api_key

def buildCallReq(audio_url, api_key):
    return 'https://api.havenondemand.com/1/api/async/recognizespeech/v1?url=' + audio_url + '&apikey=' + api_key

def buildCalJobID(jobID, api_key):
    return 'https://api.havenondemand.com/1/job/result/' + jobID +'?apikey=' + api_key

def getScore(text):
    text = text.replace(" ","+")
    http = urllib3.PoolManager()
    reqSent = http.request('POST', buildSentReq(text, '944a963d-b63c-4d65-a562-d9507ca49571'))
    jsonSent = json.loads(reqSent.data)
    return jsonSent['aggregate']['score']

    
#def getScore(text):
#    url = buildSentReq(text, '944a963d-b63c-4d65-a562-d9507ca49571')
#    result = urlfetch.fetch(url)
#    if result.status_code == 200:
#        jsonSent = json.loads(result.content)
#        return jsonSent['aggregate']['score']