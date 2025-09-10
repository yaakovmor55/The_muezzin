from elasticsearch import Elasticsearch
import config
from logger import Logger
logger = Logger.get_logger()


class ElasticCrud:

    def __init__(self, index_name=config.INDEX_NAME):
        try:
            self.es = Elasticsearch(config.ELASTIC_CONN)
            self.index_name = index_name
            logger.info(f"Connected successfully to {self.index_name}")

        except Exception as e:
            logger.error(f"Failed to connect{e}")
            self.index_name = index_name




    # Creates an index in Elasticsearch
    def create_index(self):
        try:
            if self.es.indices.exists(index=self.index_name):

                self.es.indices.delete(index=self.index_name)

            self.es.indices.create(index=self.index_name)
            logger.info(f"Index created {self.index_name}")
        except Exception as e:
            logger.error(e)


    # Inserting data to the index in Elasticsearch
    def create_data(self, doc_id, doc):
        try:
            self.es.index(index=self.index_name, id=doc_id, document=doc)
            logger.info(f"doc created {doc_id}")
        except Exception as e:
            logger.error(e)


