import tweepy
import time
import random
import numpy as np

auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")

api = tweepy.API(auth)

twts = api.search(q="facts")


limit = 10
i = 0


for s in twts:
    #for i in t:
        #if i == s.text:
    sn = s.user.screen_name
    # "@%s  " % (sn)
    m = ["@%s When a male penguin falls in love with female penguin, he searches the entire beach to find the perfect pebble to present to her." % (sn),
         "@%s It is illegal to climb trees in Oshawa, a town in Ontario, Canada." % (sn),
         "@%s  All pandas in the world are on loan from China." % (sn),
         "@%s  Dolphins recognize and admire themselves in mirrors." % (sn),
         "@%s  At room temperature, the average air molecule travels at the speed of a rifle bullet." % (sn),
         "@%s  When the moon is directly overhead, you weigh slightly less." % (sn),
         "@%s  Honeybees navigate by using the sun as a compass." % (sn),
         "@%s  Goldfish Don't have stomachs." % sn,
         "@%s  Sitting straight up is bad for your back. You should slough at an angle of 135 degrees." % sn
         ]
    s = api.update_status(np.random.choice(m), s.id)
    i += 1
    print i
    time.sleep(30 + random.randint(0, 60))
    if (i == limit):
        break






