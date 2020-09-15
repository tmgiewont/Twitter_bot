import tweepy
import time
import random

auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")

api = tweepy.API(auth)


followers = api.followers_ids("@_Freedom_bot_")
friends = api.friends_ids("@_Freedom_bot_")
i = 0
while True:
           for f in friends:
               if f not in followers:
                   api.destroy_friendship(f)
                   i += 1
                   print i
               time.sleep(30 + random.randint(0,60))

