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
#Virgin America 554395

followed = api.friends_ids('mcdickenson') # Extract IDs for those users Matt is following.
i = 0
time_between = timedelta(100) # Creating baseline of 100 for loop.
while i<len(followed): # Code below extracts 20 most recent tweets from all who Matt follows, calculates time between tweet 1 and tweet 20, and considers user with the least time elapsed "most_active."
    try:
        user = api.get_user(followed[i])
        tweets = user.timeline()
        if len(tweets) == 20: # Only making calculation for those users who have at least 20 tweets. Those with fewer than 20 tweets are not considered active.
            time_delta = tweets[0].created_at - tweets[19].created_at # Calculating time between most recent tweet and 20th tweet.
            if time_delta < time_between:
                time_between = time_delta
                most_active = str(user.name)
        i+=1
    except: time.sleep(.25) # Makes request every 0.25 seconds. Should we hit the limit, waits 0.25 before making another request. Permits for loop to remain active until limit is reset.
    
# Defining "active" in the following way: (a) extract the 20 most recent tweets from those
# who Matt follows, (b) calculate the time that has elapsed between the most recent tweet
# and the 20th one, and the follower for which the least time has elapsed is considered the
# most active user. Users who have fewer than 20 tweets we do not consider active





