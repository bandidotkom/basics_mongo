from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples

#update with save()
def main():
	city = db.cities.find_one({"name" : "München", "country" : "Germany"})
	city["isoCountryCode"] = "DEU"
	db.cities.save(city)
	
if __name__ = '__main__':
	main()

#update with update()

def find():
	city = db.cities.update({"name" : "München", "country" : "Germany"},
							{ "$set" : {"isoCountryCode" : "DEU"}
							})
	#and then unset
	city = db.cities.update({"name" : "München", "country" : "Germany"},
							{ "$unset" : {"isoCountryCode" : ""}
							})
	#this will replace whole object => do not forget parameter $set !!!
	city = db.cities.update({"name" : "München", "country" : "Germany"},
							{ "isoCountryCode" : "DEU"}
							)
if __name__ = '__main__':
	find()

#multi update
def main():
	city = db.cities.update({"country" : "Germany"},
							{"$set" : {
								"isoCountryCode" : "DEU"
								},
							multi=True
							)
	city["isoCountryCode"] = "DEU"
	db.cities.save(city)
	
if __name__ = '__main__':
	main()