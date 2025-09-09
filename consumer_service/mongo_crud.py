from pymongo.errors import PyMongoError
import logging
from pymongo import MongoClient
import gridfs
import config
from logger import Logger
logger = Logger.get_logger()

# Mongo CRUD With gridfs
class MongoCRUD:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.MONGO_DB]
        self.collection = self.db[config.COLLECTIONS]
        self.fs = gridfs.GridFS(self.db)


# Adding a file with gridfs to MongoDB
    def add_file(self, path, uniq_id):
        try:
            with open(path, 'rb') as f:
                file_id = self.fs.put(f, filename=uniq_id)
            logger.info(f"Inserted document: {uniq_id}")
            return str(file_id)
        except PyMongoError as e:
            logger.error(f"Failed to insert document: {e}")
            return None

# Reading files from MongoDB with gridfs
    def read(self, uniq_id):
        try:
            file_data = self.fs.find_one({ 'filename' : uniq_id })
            logger.info(f"Read executed: filename={uniq_id}")
            if file_data:
                with open("C:/Users/User/Downloads/nawdir/downloaded_file.wav", 'wb') as output_file:
                    output_file.write(file_data.read())
                print("File downloaded successfully")
            else:
                print("File not found")

            return file_data
        except PyMongoError as e:
            logger.error(f"Failed to read documents: {e}")
            return []

# Deleting a file with gridfs
    def delete(self, uniq_id):
        try:
            self.fs.delete(uniq_id)
            logger.info(f"delete file {uniq_id} ")
        except Exception as e:
            logger.error(f"Failed to delete file: {e}")