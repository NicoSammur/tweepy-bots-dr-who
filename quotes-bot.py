#!/usr/bin/env python
# coding: utf-8
# use: quotes-bot.py quotes.txt 

import tweepy, time, sys

file = str(sys.argv[1])

# from http://apps.twitter.com

CONSUMER_KEY = 'your_consumer_key' 
CONSUMER_SECRET = 'your_consumer_secret_key' 
ACCESS_KEY = 'your_access_token' 
ACCESS_SECRET = 'your_access_token_secret' 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

quotes=open(file,'r')
f=quotes.readlines()
quotes.close()

for line in f:
    api.update_status(line)
    # Tweet every 30 min
    time.sleep(1800) 
