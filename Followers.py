import tweepy
import time
import random

auth = tweepy.OAuthHandler("YJ5mxyUgJLmedR557EoeM3c1m","qZjccKWikCwQgcCoGqgcYvj0Pc3ai5ykLQVj19Q7ybFPU65Sgj")
auth.set_access_token("753680282977525760-UGdZfSS4YdxEeH8bYc7PwLi6uMIQmuk","VutjO8k5QITPjvKtowKVr12LXrsUKsuMArVmSlXiIv0wP")

api = tweepy.API(auth)

accountvar = raw_input("Account name: ")

users = tweepy.Cursor(api.followers, screen_name=accountvar).items()

i = 0
while True:
   try:
       i += 1
       user = next(users)
       user = next(users)
       api.create_friendship(user.screen_name)
       print i
       time.sleep(60 + random.randint(0,60))
   except:
       time.sleep(60*15)
       pass





