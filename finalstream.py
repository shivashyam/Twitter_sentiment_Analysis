# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:20:21 2018

@author: siva
"""

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob

ckey="kn02RmpS8B9hTKG3qErdPhBIZ"
csecret="5gR1udhDZ5tzLgk24mKAAiPMANac8IJvw2ubjdAD8pY2mNhExs"
atoken="563566303-Y5Ztmck0vJufcQtOt2xDWui2pQyaoPj7PMHvCo07"
asecret="SgqeJC9HaxrXiUxYgPT4HQevjJ9GJBnheLSRRduG0yvbw"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

public_tweets = api.search('car')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)