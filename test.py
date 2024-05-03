'''
this file outputs the total document count and clears the dataproject2 collection
'''

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

# connect to mongodb
MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
#specifying database
db = client.zy7ts
collection = db.dataproject2

document_count = collection.count_documents({})
print(document_count)

collection.drop()

document_count = collection.count_documents({})
print(document_count)