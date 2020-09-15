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


#api = tweepy.API(auth)
api = tweepy.API(auth,wait_on_rate_limit=True)
#gets num amount of tweets with the given hashtag to be used later
hashtag = raw_input("Enter Hashtag: ")
num = input("How many tweets: ")
tweet_list = []
tweet_seen = []
tweet_train = []


def clean(temp):
    clean = []
    for word in temp:
        stopwords =['@', 'RT', "\n", "retweet", "&amp", "a", "our", "only"]
        querywords = word.split()
        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        clean.append(result)

    return clean

pos = open("pos_tweets.txt", 'r')
neg = open("neg_tweets.txt", 'r')

train = ([(p_tweet.decode('utf-8'), 'pos') for p_tweet in pos] +[(n_tweet.decode('utf-8'), 'neg') for n_tweet in neg])

cl = NaiveBayesClassifier(train)
#Extracts the tweets that have the given hashtag
results = api.search(q=hashtag, lang="en", count=num, tweet_mode="extended")
for tweet in results:
    if hasattr(tweet, 'retweeted_status'):
        tweet_list.append(tweet.retweeted_status.full_text.encode('utf-8'))
    else:
        tweet_list.append(tweet.full_text.encode('utf-8'))

i = 0
correct =0
tot = 0
pos_tweet = []
neg_tweet = []
tweet_list = list(set(tweet_list))
while (i <  len(tweet_list)):
    tweet1 = tweet_list[i]
    while tweet1 in tweet_seen:
        i += 1
        tweet1 = tweet_list[i]
    tweet1 = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b|\n|@', '', tweet1, flags=re.MULTILINE)
    print tweet1
    print cl.classify(tweet1.decode('utf-8'))
    judge = input("1 pos, 2 neg, 3 skip, 4 break: ")
    if judge == 1:
        pos_tweet.append(tweet1)
    elif judge == 2:
        neg_tweet.append(tweet1)
    elif judge == 4:
        break
    tweet_seen.append(tweet1)
    if cl.classify(tweet1.decode('utf-8'))== 'pos' and judge == 1:
        correct += 1
    if cl.classify(tweet1.decode('utf-8')) == 'neg' and judge == 2:
        correct +=1
    if judge != 3:
        tot +=1

    i += 1

print "Average = ", (float)(correct)/tot
pos = open("pos_tweets.txt", "a")
neg = open("neg_tweets.txt", "a")
pos_tweet = clean(pos_tweet)
neg_tweet = clean(neg_tweet)
for z in pos_tweet:
        pos.write("%s\n" % z)
for x in neg_tweet:
        neg.write("%s\n" % x)
pos.close()
neg.close()
