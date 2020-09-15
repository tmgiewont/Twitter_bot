import tweepy
import time
import random
import numpy as np

auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")

api = tweepy.API(auth)

Tweet_list = [ "Stay true to America", "We need more american pride"]
hashtag = [ " #Trump", " #Hillaryforprison", " #MakeAmericaGreatAgain", " #TrumpPence2016" ]
hashtag_search = [ " #Trump", " #Hillaryforprison", " #MakeAmericaGreatAgain", " #TrumpPence2016",
                  " #hillary", " #hillary2016", " #never" ]
while True:
   for status in api.search (q=hashtag, count = 1):
       # Process a single status

       user_id = (status.user.id)
       user = api.get_user(user_id)
       status_id = (status.id)
       print (user.screen_name)
       print(status.text)
       new_tweet = "@" + user.screen_name + ((np.random.choice(Tweet_list) + np.random.choice(hashtag)))
       print new_tweet
       try:
           #api.update_status(new_tweet)
           time.sleep(30 + random.randint(0,60))
       except:
           pass

           time.sleep(5)






