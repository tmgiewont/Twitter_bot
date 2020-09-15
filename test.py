import tweepy

auth = tweepy.OAuthHandler("") #consumer key,consumer secret
auth.set_access_token("") #acess token,acess token secret

api = tweepy.API(auth)

api.update_status("Republish if You Love America")

