from pymongo.errors import PyMongoError
import logging
from pymongo import MongoClient
import gridfs
import config

class MongoCRUD:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.MONGO_DB]
        self.collection = self.db[config.COLLECTIONS]
        self.fs = gridfs.GridFS(self.db)



    def add_file(self, path, uniq_id):
        try:
            with open(path, 'rb') as f:
                file_id = self.fs.put(f, filename=uniq_id)
            logging.info(f"Inserted document: {uniq_id}")
            return str(file_id)
        except PyMongoError as e:
            logging.error(f"Failed to insert document: {e}")
            return None






    def read(self, query):
        try:
            results = list(self.collection.find(query))
            logging.info(f"Read executed: Query={query}")
            return results
        except PyMongoError as e:
            logging.error(f"Failed to read documents: {e}")
            return []

    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            logging.info(f"Updated documents where {query} with {update_data}")
            return result.modified_count
        except PyMongoError as e:
            logging.error(f"Failed to update documents: {e}")
            return 0

