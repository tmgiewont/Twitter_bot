import tweepy
import time
import random
import sys
import logging

auth = tweepy.OAuthHandler()
auth.set_access_token()

api = tweepy.API(auth)

accountvar = sys.argv[1]

# accountvar = raw_input("Account name: ")

users = tweepy.Cursor(api.followers, screen_name=accountvar).items()
logging.basicConfig(filename='Followers.log',level=logging.DEBUG)
i = 0
while True:
   try:
       i += 1
       user = next(users)
       user = next(users)
       api.create_friendship(user.screen_name)
       print i , user.screen_name
       logging.info('%s, %s', i, user.screen_name)
       time.sleep(60 + random.randint(0,60))
   except:
       time.sleep(60*15)
       pass





