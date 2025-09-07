PODCASTS_TOPIC = "podcasts_topic"
BOOTSTRAP_SERVERS = 'localhost:9092'
ELASTIC_CONN="http://localhost:9200"
INDEX_NAME="podcasts"

CUSTOM_MAPPING = {
    "properties": {
        "podcastID": {"type": "float"},
        "metadata": {
            "type": "dict",
        }
    }
}

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "tweets_db"
COLLECTIONS = {
    "podcasts": "podcasts",
}
