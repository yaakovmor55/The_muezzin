from pymongo.errors import PyMongoError
import logging

class MongoCRUD:
    def __init__(self, conn, db_name, collection_name):
        self.conn = conn
        self.db = self.conn[db_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            logging.info(f"Inserted document: {data}")
            return str(result.inserted_id)
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