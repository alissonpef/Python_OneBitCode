from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

post1 = {
     "title": "Web Scraping",
     "category": "Automação",
     "author": {
         "name": "fds",
         "email":"fulano@email.com"
    },
}

result = mycol.insert_one(post1)