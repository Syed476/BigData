import requests
import pymongo
from pymongo import MongoClient

cluster =MongoClient('mongodb+srv://shah476:Shahjee1977@cluster0.dq7wl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["test"]
collection=db["test"]

#post1={"_id":40,"name":"mike","score":6}
#post2={"_id":31,"name":"john","score":7}
#collection.insert_many([post1,post2])

results=[]
for i in range(9):

	url = "https://countries-cities.p.rapidapi.com/location/city/nearby"

	querystring = {"latitude":"55.11","longitude":"37.02","radius":"25","min_population":"99","max_population":"10000"}

	headers = {
    	'x-rapidapi-host': "countries-cities.p.rapidapi.com",
    	'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	results.append(response.json())

collection.insert_many(results)
