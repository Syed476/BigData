import pymongo
from pymongo import MongoClient

cluster=MongoClient('')
cluster =MongoClient('mongodb+srv://shah476:Shahjee1977@cluster0.dq7wl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster["test"]
collection=db["test"]

post={"id":0,"name":"syed","score":6}
collection.insert_1(post)
