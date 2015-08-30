import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['30']
topics = db.topics
posts = db.posts

def getTopics():
	return topics

def getPosts():
	return posts