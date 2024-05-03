# setup
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

# connection 
MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
#specifying database
db = client.zy7ts
collection = db.dataproject2

directory = 'data'

#looping through files
for filename in os.listdir(directory):
    #loading json files
    with open (os.path.join(directory, filename)) as f:
        try:
            file_data = json.load(f)
        except Exception as e:
            print('!!loading error!!', e, 'error when loading', f, '\n')
    #inserting into DB
    if isinstance(file_data, list):
      try:
        collection.insert_many(file_data)
      except Exception as e:
        print('!!insert error!!', e, "error when importing into Mongo", '\n')
    else:
      try:
        collection.insert_one(file_data)
      except Exception as e:
        print('!!insert error!!', e, '\n')
