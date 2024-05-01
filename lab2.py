# setting up
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

# connect to mongodb
MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

db = client.zy7ts
collection = db.dataproject2

# looping thorugh files & inserting into DB
path = "data"
for (root, dirs, file) in os.walk(path):
    for f in file:
        path = os.path.join(root, f)
        with open(path) as file:
            file_data = json.load(file)
            if isinstance(file_data, list):
                collection.insert_many(file_data)
            else:
                collection.insert_one(file_data)