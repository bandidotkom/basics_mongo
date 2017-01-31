from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def hashtag_retweet_avg():
	result = db.tweets.aggregate([
			{"$unwind" : "$entities.hashtags"},
			{"$group" : {"_id" : "$entities.hashtags.text", "retweet_avg" : {"$avg" : "$retweet_count"}}},
			{"$sort" : {"retweet_avg" : -1}}]
		)
	return result

if __name__ = '__main__':
	result = hashtag_retweet_avg()
	pprint.pprint(result)