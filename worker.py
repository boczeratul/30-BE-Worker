import datetime
import time
import database
import classes

interval = 5 * 60

def main():
    while True:
        # postDicts must be sorted according to create time
        postDicts = database.getPostCollection().find()
        classes.parseTopics(postDicts)

        topics = classes.topics
        # for topic in topics:
        #     print topic._id + ' ' + str(topic.heat)

        posts = classes.posts
        # for post in posts:
        #     print post._id + ' ' + str(post.heat)

        database.setTopicCollection(topics)
        database.updatePostCollection(posts)

        timestamp = int(time.time())
        print '[' + str(datetime.datetime.fromtimestamp(timestamp)) + '] processed database'
        time.sleep(interval)

if __name__ == "__main__":
    main()