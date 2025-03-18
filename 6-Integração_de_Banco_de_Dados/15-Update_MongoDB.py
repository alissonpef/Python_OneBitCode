from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = { "category": "Data Science" }
newvalues = { "$set": { "category": "Data Analysis" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)
