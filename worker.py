import database
import datetime
import time
import classes

def main():  
    # postDicts must be sorted according to create time
    postDicts = database.getPostCollection().find()
    classes.parseTopics(postDicts)

    topics = classes.topics
    for topic in topics:
        print topic._id + ' ' + str(topic.heat)

    posts = classes.posts
    for post in posts:
        print post._id + ' ' + str(post.heat)

    database.setTopicCollection(topics)
    database.updatePostCollection(posts)

if __name__ == "__main__":
    main()