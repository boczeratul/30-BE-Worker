## System Setup:
1. [MongoDB](http://docs.mongodb.org/manual/installation/) (Database)
2. [Java 8](http://www.oracle.com/technetwork/java/javase/downloads/index.html) 
3. [RESTHeart](https://github.com/SoftInstigate/RESTHeart/releases) (Web API for MongoDB)
4. [python](https://www.python.org/downloads/) (Back-End Worker)
5. [pymongo](http://api.mongodb.org/python/current/installation.html) (Back-End Worker)

## Web API:
1. Insert  
`PUT http://127.0.0.1:8080/30/topics/<id>`
2. Update  
`PUT http://127.0.0.1:8080/30/topics/<id> with If-Match header`  

[RESTHeart API Docs](https://softinstigate.atlassian.net/wiki/display/RH/6.+API)
