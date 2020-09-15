from textblob.classifiers import NaiveBayesClassifier
import re
import nltk
import json
nltk.download('punkt')
from nltk import word_tokenize
import tweepy
import re
auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")

#Gets tweets under a certain hashtag and then will run them through the model and extract the tweets that are considered
#conservative and stores them into a list to be retweeted later
api = tweepy.API(auth,wait_on_rate_limit=True)
hashtag = raw_input("Enter Hashtag: ")
num = input("How many tweets: ")

tweet_list = []
tweet_train = []
source = []
tweet_id = []

pos = open("pos_tweets.txt", 'r')
neg = open("neg_tweets.txt", 'r')

#Sets up the Classifier using the previously downloaded tweets
train = ([(p_tweet.decode('utf-8'), 'pos') for p_tweet in pos] +[(n_tweet.decode('utf-8'), 'neg') for n_tweet in neg])
cl = NaiveBayesClassifier(train)
#opens a file to store the tweet ids to later used to retweet
ids = open("id.txt", "a")

#finds num amount of tweets based on a hashtag

results = api.search(q=hashtag, lang="en", count=num, tweet_mode="extended")
for tweet in results:
    if hasattr(tweet, 'retweeted_status'):
        tweet_list.append(tweet.retweeted_status.full_text.encode('utf-8'))
    else:
        tweet_list.append(tweet.full_text.encode('utf-8'))
    source.append(tweet)

i = 0
tweet_list = list(set(tweet_list)) #removes duplicates
while (i <  len(tweet_list)):
    tweet1 = tweet_list[i]
    tweet1 = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b|\n|@', '', tweet1, flags=re.MULTILINE)
    if cl.classify(tweet1.decode('utf-8'))== 'pos':  #if the classifier thinks the tweet is positive it writes the id to a file
        ids.write("%s\n" % source[i].id)
    i += 1



ids.close()
