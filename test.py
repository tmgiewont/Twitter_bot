import tweepy

auth = tweepy.OAuthHandler("YJ5mxyUgJLmedR557EoeM3c1m","qZjccKWikCwQgcCoGqgcYvj0Pc3ai5ykLQVj19Q7ybFPU65Sgj") #consumer key,consumer secret
auth.set_access_token("753680282977525760-UGdZfSS4YdxEeH8bYc7PwLi6uMIQmuk","VutjO8k5QITPjvKtowKVr12LXrsUKsuMArVmSlXiIv0wP") #acess token,acess token secret

api = tweepy.API(auth)

api.update_status("Republish if You Love America")

