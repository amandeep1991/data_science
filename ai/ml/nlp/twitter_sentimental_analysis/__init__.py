import tweepy


# Access Tokens
consumer_key = '3iSi24XvrOU0flfOVfuW8bGSc'
consumer_secret = 'OyN9eQXjyYSd5JGeNsxTm3ZZPfYVmGUOvdOepaPA5rwnZaiPXc'
access_token = '954263969178398721-yoUZbU1mThZxTt7Dj3teEXDqTDG30Ht'
access_token_secret = 'bz9GcuvcwlMLAXqJlzGHYdBFa56WHgGqtOhrkeSmxGrxK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)