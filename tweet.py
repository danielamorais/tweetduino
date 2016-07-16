#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyleft © 2016 danielamorais <danielamorais@tars>
#
# Distributed under terms of the GNU GPL license.

from twython import Twython
 
 APP_KEY = 'key' # Customer Key here
 APP_SECRET = 'secret key' # Customer secret here
 OAUTH_TOKEN = 'access token' # Access Token here
 OAUTH_TOKEN_SECRET = 'token secret' # Access Token Secret here
  
 twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
   
 var_status=raw_input('enter your tweet'); #accepts input you can type your tweet
 twitter.update_status(status=var_status); #you can check twitter to see your tweet live 

