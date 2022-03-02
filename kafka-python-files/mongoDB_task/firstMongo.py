import pymongo
from pymongo import MongoClient

cluster =MongoClient('mongodb+srv://shah476:Shahjee1977@cluster0.dq7wl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["test"]
collection=db["test"]

post1={"_id":40,"name":"mike","score":6}
post2={"_id":31,"name":"john","score":7}
collection.insert_many([post1,post2])
