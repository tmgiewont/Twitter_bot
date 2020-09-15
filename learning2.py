from textblob.classifiers import NaiveBayesClassifier
import re
import nltk
import json
nltk.download('punkt')
from nltk import word_tokenize

pos = open("pos_tweets.txt", 'r')
neg = open("neg_tweets.txt", 'r')

train = ([(p_tweet.decode('utf-8'), 'pos') for p_tweet in pos] +[(n_tweet.decode('utf-8'), 'neg') for n_tweet in neg])
#print train

#this is more data that is used to test the training set of data
test1 = [
    ("We need to deport all the illegal immigrants #BuildTheWall #RedWave #trump2020", "pos"),
    ("Trump is an embarassment to our country and we need to impeach him #ImpeachTrump #NotMyPresident", "neg"),
    ("So much corruption around Trump he is a proven liar #TrumpIsALiar", "neg"),
    ("The Liberal media is falsely representing trump #FakeNews", "pos"),
    ("Trump is a racist and needs to be impeached #notmypresident", "neg"),
    ("This country is much better under Trump #MAGA #trump2020", "neg"),
    ("We can't let the government take our guns away #NRA #MAGA", "pos"),
    ("Wake up America, Trump is corrupt #impeachTrump", "neg")



]

#run the cleanTweets function to remove useless words


#run the classifier and train the data
cl = NaiveBayesClassifier(train)

# Classify some text
print '--------------'

#test out the trained data set. Will return what type of tweet it thinks it is
print(cl.classify("Impeach Trump #ImpeachTrump"))  # "neg"
print(cl.classify("Vote Trump 2020 #Trump2020"))
print(cl.classify("We can't let the government take our guns away #NRA #MAGA"))# "pos"
print '--------------'

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test1)))

# Show 5 most informative features
cl.show_informative_features(10)



