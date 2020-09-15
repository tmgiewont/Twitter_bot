import tweepy
import time
import numpy as np
import random

auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")

api = tweepy.API(auth)
Tweet_list = ["Trump is the man who will deal with ISIS",
              "Hillary was not qualified for the role as president ",
             "Why do people want illegal immigrants?",
              "Fewer people are showing their american pride",
             "If you don't love the country you live in then leave it!",
             "How exactly is trying to protect the American people by securing our borders racist?",
              "How much longer can we be forced to listen to the biased liberal media?",
              "We need more unity in our country we can't be divided",
              "Republish If You Think America Is The Best Country Ever!!",
              "We Need More Pride and Respect for Our Country Republish If you Agree!!"
              , "What are Your opinions on Trump's View on Climate Change? Do You agree or Disagree?  "]


hashtag = [" #trump",  " #Trump 2016", " #republican", " #USA",
            " #2016", " #TrumpPence2016", " #DonaldTrump", " #GreatestCountry", " #WethePeople",
            "#America", "#IloveAmerica" ]



random.shuffle(Tweet_list)
random.shuffle(hashtag)
n =0
while True:
       try:
           Tweet = Tweet_list[n] + hashtag[n]
           #Tweet = ((np.random.choice(Tweet_list) + np.random.choice(hashtag)))
           if len(Tweet) >= 140:
               continue
           else:
               api.update_status(Tweet)
               print(Tweet)
               n +=1
               time.sleep(60 + random.randint(0,60))
               if(n == len(Tweet_list)):
                   random.shuffle(Tweet_list)
                   random.shuffle(hashtag)
                   n = 0
       except:
           pass




