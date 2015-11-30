# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:18:54 2015

@author: prcobol
"""

import requests
import json
#from havenondemand.hodindex import HODClient



def buildSentReq(text, api_key):
    return 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=' + text + '&apikey=' + api_key

def buildCallReq(audio_url, api_key):
    return 'https://api.havenondemand.com/1/api/async/recognizespeech/v1?url=' + audio_url + '&apikey=' + api_key

def buildCalJobID(jobID, api_key):
    return 'https://api.havenondemand.com/1/job/result/' + jobID +'?apikey=' + api_key

def getScore(text):
    reqSent = requests.post(buildSentReq(text, '944a963d-b63c-4d65-a562-d9507ca49571'))
    jsonSent = json.loads(reqSent.content)
    return jsonSent['aggregate']['score']


