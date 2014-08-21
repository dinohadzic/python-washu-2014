# HW6
# Dave Carlson and Dino Hadzic

import time
from datetime import timedelta

followers = api.followers_ids('mcdickenson') # Extract IDs for Matt's followers.
followers_count = 0 # Creating baseline of 0 followers.
i=0
while i<len(followers): # Code below loops through all users who follow Matt, and continues to update who stored as the "most_followed" as loop runs.
    try:
        user = api.get_user(followers[i])
        if user.followers_count > followers_count:
            followers_count = user.followers_count
            most_followed = str(user.name)
        i+=1
    except: time.sleep(.25) # Makes request every 0.25 seconds. Should we hit the limit, waits 0.25 before making another request. Permits for loop to remain active until limit is reset.


followed = api.friends_ids('mcdickenson') # Extract IDs for those users Matt is following.
i = 0
max_tweets = 0 # Creating baseline for number of tweets.
while i<len(followed): # Code below counts total tweets of each followed
    try:
        user = api.get_user(followed[i])
        tweets = user.statuses_count
        if max_tweets < tweets:
            max_tweets = tweets
            most_active = str(user.name)
        i+=1
    except: time.sleep(.25) # Makes request every 0.25 seconds. Should we hit the limit, waits 0.25 before making another request. Permits for loop to remain active until limit is reset.

print most_followed #Virgin America 554395
print most_active #Matt Yglesias
    
# Defining "active" as most total tweets




