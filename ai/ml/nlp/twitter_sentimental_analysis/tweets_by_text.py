#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import time
from ml.nlp.twitter_sentimental_analysis import auth

# Twitter API credentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# refer http://docs.tweepy.org/en/v3.2.0/api.html#API
# tells tweepy.API to automatically wait for rate limits to replenish

# Put your search term
searchquery = "data protection"

users = tweepy.Cursor(api.search, q=searchquery).items()
count = 0
errorCount = 0

file = open('search.json', 'w')

while True:
    try:
        user = next(users)
        count += 1
        # use count-break during dev to avoid twitter restrictions
        # if (count>10):
        #    break
    except tweepy.TweepError:
        # catches TweepError when rate limiting occurs, sleeps, then restarts.
        # nominally 15 minnutes, make a bit longer to avoid attention.
        print
        "sleeping...."
        time.sleep(60 * 16)
        user = next(users)
    except StopIteration:
        break
    try:
        print("Writing to JSON tweet number:" + str(count))
        # json.dump(page._json, bytes(file.__str__(), 'utf-8'), sort_keys=True, indent=4)
        json.dump(user._json, file)
        # print(file)

    except UnicodeEncodeError:
        errorCount += 1
        print("UnicodeEncodeError,errorCount =" + str(errorCount))

print("completed, errorCount =" + str(errorCount) + " total tweets=" + str(count))

# todo: write users to file, search users for interests, locations etc.

"""
http://docs.tweepy.org/en/v3.5.0/api.html?highlight=tweeperror#TweepError
NB: RateLimitError inherits TweepError.
http://docs.tweepy.org/en/v3.2.0/api.html#API  wait_on_rate_limit & wait_on_rate_limit_notify
NB: possibly makes the sleep redundant but leave until verified.

"""