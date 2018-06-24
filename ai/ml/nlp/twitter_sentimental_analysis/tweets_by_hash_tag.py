import tweepy
import csv


# Creating twitter API object
from ml.nlp.twitter_sentimental_analysis import auth

api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/Create a file to append data (a below stands for append mode)
with open('ua.csv', 'a', newline='') as csvFile:
    # Use csv Writer (We used a writer to append data in junks so that it
    # doesn't need to maintain all data in RAM, it takes a line/tweet and write it onto file and so on)
    csvWriter = csv.writer(csvFile)
    # Seems like this 'unitedAIRLINES' is the page where people tweets and it is fetching tweets since "2018-05-25" and
    # will return top 100 tweets
    for tweet in tweepy.Cursor(api.search, q="#unitedAIRLINES", count=100, lang="en", since="2018-05-25").items():
        print('#[[[[[#', tweet.created_at, tweet.text, '#]]]]]#')  # printing each tweet text on console
        csvWriter.writerow([tweet.created_at, str(tweet.text).encode('utf-8')])  # write the tweet on the csv file
        break