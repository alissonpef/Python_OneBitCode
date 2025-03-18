from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

#result = mycol.find_one()
result = mycol.find()

for r in result:
    pprint(r)

#pprint(result)
