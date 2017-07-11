import tweepy
import time
import random

auth = tweepy.OAuthHandler("YJ5mxyUgJLmedR557EoeM3c1m","qZjccKWikCwQgcCoGqgcYvj0Pc3ai5ykLQVj19Q7ybFPU65Sgj")
auth.set_access_token("753680282977525760-UGdZfSS4YdxEeH8bYc7PwLi6uMIQmuk","VutjO8k5QITPjvKtowKVr12LXrsUKsuMArVmSlXiIv0wP")

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

