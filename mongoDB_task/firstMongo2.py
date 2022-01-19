import requests
import pymongo
from pymongo import MongoClient

cluster =MongoClient('mongodb+srv://shah476:Shahjee1977@cluster0.dq7wl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["test"]
collection=db["test"]

#post1={"_id":40,"name":"mike","score":6}
#post2={"_id":31,"name":"john","score":7}
#collection.insert_many([post1,post2])

#collection.insert_many(results)
# Showing all data from the Database test

results=collection.find({})

for result in results:
	print(result)

# Querying the data on different rows
print ("="*30)
results1=collection.find({"cities.population":151})

print(results1)

for el in results1:
	print(el)
