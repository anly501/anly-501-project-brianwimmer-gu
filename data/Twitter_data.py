#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:56:22 2022

@author: brianwimmer
"""

import pandas as pd
import os
import time
import requests
import json
import csv
from tqdm import tqdm

import tweepy

import requests
import pandas as pd
import os

api = pd.read_csv("/Users/brianwimmer/Desktop/Georgetown/ANLY 501/Twitter_API.txt")

# Get keys
consumer_key        = api.iloc[0]['Key']
consumer_secret     = api.iloc[1]['Key']
access_token        = api.iloc[3]['Key']
access_token_secret = api.iloc[4]['Key']
bearer_token        = api.iloc[2]['Key']

# Authorization and Bearer Token
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
headers = {"Authorization": "Bearer {}".format(bearer_token)}
print()

# Search twitter
def search_twitter(query, tweet_fields, bearer_token, max_results, start_time, end_time):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&max_resuls={}&start_time={}&end_time={}".format(query, tweet_fields, max_results, start_time, end_time)
    
    print("--------------",url,"--------------")
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    # print(response.text)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# search term
query = "airlines"

# twitter fields to be returned by api call
tweet_fields = "tweet.fields=text,author_id,created_at,lang"

# maximum results
max_results = 100

# timing -> day of first bailout march 27
start_time = "2020-03-27T16:22:02+00:00"
end_time = "2020-03-28T16:22:02+00:00"


# twitter api call ***** and combine
json_response_airlines = search_twitter(query, tweet_fields, bearer_token, max_results=max_results, start_time=start_time, end_time=end_time)


print(json.dumps(json_response_airlines, indent=4, sort_keys=True))















