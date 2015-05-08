from TwitterSearch import *
import csv
import re
import pickle as Pickle
from textblob.classifiers import NaiveBayesClassifier
import codecs
import sys 
if __name__ == '__main__':
    
    
    print ("hello")
    print("loading classifiers....")
    #first train and save save the classifier(train()),then load the classifier(classify())
    #train()
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(['kfc']) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
                           consumer_key = '5gnQuvbPX8v0Pu7xlyolQ3SCf',
                           consumer_secret = '8M4uuXpv9po5Bg5XYWGKKS1kJzAL24t6nl7mwEzig6ro6YPAtC',
                           access_token = '1248339090-EtmyDYrZ0mBXgumwBAaX5tLfc9mexVN5uh89IAf',
                           access_token_secret = 'S6Nm6MaYu79bSjQuhZMmWoFhLbF2yLHvwBqZghsm3GuFN'
                           )                     
        s=''
        sentiment = Pickle.load( open( "./sentiment.pickle2", "rb" ) )
        emotion = Pickle.load( open( "./emotion.pickle2", "rb" ) )
        issue = Pickle.load( open( "./issue.pickle2", "rb" ) )
        
        # this is where the fun actually starts :)
        count=0
        
        for tweet in ts.search_tweets_iterable(tso):
            sequence=tweet['text']
            label=sentiment.classify(sequence)
            label2=emotion.classify(sequence)
            label3=issue.classify(sequence)
            prob_dist1 = sentiment.prob_classify(sequence)
            prob_dist2 = emotion.prob_classify(sequence)
            count=count+1
            print("Number",count)
            p1=round(prob_dist1.prob(prob_dist1.max()), 2)#round(prob_dist.prob("pos"), 2)
            p2=round(prob_dist2.prob(prob_dist2.max()), 2)
            print(p1)
            print(p2)
            print(tweet['text'].encode('utf8'))
            print(re.sub(u"[^a-zA-Z ]","",tweet['text']))
            newLine=re.sub(u"[^a-zA-Z ]","",tweet['text'])
            print(label," ",label2," ",label3)
            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            try:
                with open('./needtoVis.csv', 'a', newline='') as fp:
                    
                    a = csv.writer(fp, delimiter=',')
                    data=[[newLine,label,label2,label3]]
                    try:
                        a.writerows(data)
                        fp.flush
                    finally: 
                        fp.close
            except IOError:
                print("file opening exception")
            
            if p1<0.5 or p2<0.5:    
                try:
                    with open('D:/train/uncertain.csv', 'at',newline='',encoding='utf-8') as fp:
                        spamwriter = csv.writer(fp, delimiter=',')
                        uncertain=tweet['text']
                        try:
                            spamwriter.writerows([[uncertain.replace(u"\n",u" ")]])
                            fp.flush
                        finally: 
                            fp.close
                except IOError:
                    print("uncertain file opening exception")
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)