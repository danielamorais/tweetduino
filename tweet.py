#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyleft © 2016 danielamorais <danielamorais@tars>
#
# Distributed under terms of the GNU GPL license.

from twython import Twython
from flask import Flask
import apiConfig

app = Flask(__name__)

APP_KEY = apiConfig.APP_KEY # Customer Key here
APP_SECRET = apiConfig.APP_SECRET # Customer secret here
OAUTH_TOKEN = apiConfig.OAUTH_TOKEN  # Access Token here
OAUTH_TOKEN_SECRET = apiConfig.OAUTH_TOKEN_SECRET # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
   
@app.route("/sendTweet/<message>")
def sendTweet(message):
    twitter.update_status(status=message); #you can check twitter to see your tweet live 
    return "Done." 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
