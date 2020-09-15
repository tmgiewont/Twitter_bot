import tweepy
import re
import time
import random
auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")

#api = tweepy.API(auth)
api = tweepy.API(auth)
#Goes through the list of previously extracted tweets and retweets them.
ids = open("id.txt", "r")
tweets=[]
for x in ids:
    tweets.append((int)(x))
ids.close()
for i in tweets:
    #time.sleep(60 + random.randint(0, 60))
    try:
        api.retweet(i)
        tweets.remove(i)
    except:
        pass
ids = open("id.txt", "w")  #clears out file for reuse
