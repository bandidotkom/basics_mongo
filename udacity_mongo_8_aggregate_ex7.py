from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def unique_hashtags_by_user():
	result = db.tweets.aggregate([
		{"$unwind" : "$entities.hashtags"},
		{"$group" : {"_id" : "$user.screen_name",
					 "unique_hashtags" : {
								"$addToSet" : "$entities.hashtags.text"}}},
		{"$sort" : {"_id" : -1}}])
	return result

if __name__ = '__main__':
	result = unique_hashtags_by_user()
	pprint.pprint(result)