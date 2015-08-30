import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['30']
topicColl = db.topics
postColl = db.posts

def setTopicCollection(topics):
    topicColl.remove()
    for topic in topics:
        topicDoc = {
            "_id": topic._id,
            "heat": topic.heat
            }
        topicColl.insert_one(topicDoc)

def getPostCollection():
    return postColl

def updatePostCollection(posts):
    for post in posts:
        postColl.update_one({"_id": post._id}, {'$set': {"heat": post.heat, "topic": post.topic._id}})