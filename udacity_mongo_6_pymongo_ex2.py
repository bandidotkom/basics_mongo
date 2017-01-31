from pymongo import MongoCLient
import pprint

client = MongoClient('mongodb://localhost:27017/')

db = client.examples

d.autos.insert(tesla_s)
def find():
	autos =  db.autos.find({"manufacturer" : "Toyota"})
	for a in autos:
		pprint.pprint(a)

if __name__ == '__main__':
	find()