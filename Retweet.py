import tweepy
import re
import time
import random
auth = tweepy.OAuthHandler("YJ5mxyUgJLmedR557EoeM3c1m","qZjccKWikCwQgcCoGqgcYvj0Pc3ai5ykLQVj19Q7ybFPU65Sgj")
auth.set_access_token("753680282977525760-UGdZfSS4YdxEeH8bYc7PwLi6uMIQmuk","VutjO8k5QITPjvKtowKVr12LXrsUKsuMArVmSlXiIv0wP")

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
