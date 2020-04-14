from pymongo import MongoClient
def makeConnection():
    client = MongoClient('localhost:27017')
    db = client.ContactDB
    return db