import array
import time

topics = []
topicMap = {}
posts = []
postMap = {}

class Post:
    def __init__(self, dict):
        self._id = dict.get('_id')
        self.timestamp = dict.get('timestamp', time.time())
        self.parent_id = dict.get('parent', '')
        self.children = []
        self.heat = 0

    def addChild(self, child_id):
        self.children.append(child_id)

    def setTopic(self, topic):
        self.topic = topic

    def setParent(self, parent):
        self.parent = parent

    def getHeat(self):
        timeWeekAgo = time.time() - 7 * 24 * 60 * 60
        heat = self.timestamp - timeWeekAgo
        if (heat < 0):
            heat = 0
        return heat

    def addHeat(self, heat):
        if (self.parent_id):
            self.parent.addHeat(0.5 * heat)
        self.heat += heat

class Topic:
    def __init__(self, _id):
        self._id = _id
        self.heat = 0

    def addHeat(self, heat):
        self.heat += heat

def parseTopics(postDicts):
    global topics
    global topicMap
    global posts
    global postMap

    # clear data
    topics = []
    topicMap = {}
    posts = []
    postMap = {}

    for postDict in postDicts:
        post = Post(postDict)
        
        if post.parent_id != '':
            topic = topicMap.get(post.parent_id)
            topicMap[post._id] = topic
        else:
            topic = Topic(post._id)
            topics.append(topic)
            topicMap[post._id] = topic

        post.setTopic(topic)
        post.setParent(postMap.get(post.parent_id))
        topic.addHeat(post.getHeat())
        post.addHeat(post.getHeat())
        posts.append(post)
        postMap[post._id] = post