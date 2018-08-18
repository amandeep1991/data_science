import datetime
import json
import urllib

import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.reddit

stories = db.stories


def get_and_load_data_from_web():
    reddit_page = urllib.request.urlopen("http://www.reddit.com/r/technology/.json")
    print(reddit_page)
    parsed = json.loads(reddit_page.read().decode())
    for item in parsed['data']['children']:
        stories.insert_one(item['data'])
        print("Inserted: ", item['data']['name'])
    # stories.insert_many([ item['data'] for item in parsed['data']['children']], order=True) #insert many option
    print("Json Document Uploaded Successfully!!")


# get_and_load_data_from_web()

query = {
    'title': {
        '$regex'  : 'apple|google',
        '$options': 'i'
        }
    }  # option i means case-insensitive
projections = {
    'ups'  : 1,
    'title': 1,
    'score': 1,
    '_id'  : 0
    }

# sort, skip, limit have the precedence order as mentioned in the line
try:
    cursor = stories.find(query, projections).sort('ups', pymongo.DESCENDING).skip(2)
    # cursor = stories.find(query, projections).sort([('ups', pymongo.DESCENDING), ('score', pymongo.ASCENDING)]).skip(2).limit(2)
    # inside sort pass array of tuples but in shell we pass dictionary, the reason being dictionary are not ordered in python
except Exception as e:
    print("Unexpected Error Occured", type(e), e)

for doc in cursor:
    print(doc)

result = stories.update_one({}, {
    '$set': {
        'review_date': datetime.datetime.utcnow()
        }
    })

print("Numbers Matched: ", result.matched_count)

result = stories.update_many({}, {
    '$set': {
        'review_date': datetime.datetime.utcnow()
        }
    })

print("Numbers Matched: ", result.matched_count)

# stuff.replace_one({"name":'aman'}, {'friend':'ball', 'cousin':'glove'}, upsert=True) -> it willn't contain name in the output
# stuff.replace_one({'_id':'bat'}, {'friend':'ball', 'cousin':'glove'}, upsert=True) -> it will contain the _id in the output
# delete_result = delete_one(filter)
# delete_result = delete_many(filter)

# to atomically find and update a document
# counters.find_one_and_update(filter={
#     'type': name
#     }, update={
#     "$inc": {
#         'value': 1
#         }
#     },
#         upsert=True,
#         return_document=pymongo.ReturnDocument.AFTER
#         )