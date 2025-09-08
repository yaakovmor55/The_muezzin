from elasticsearch import Elasticsearch
import config
from logger import Logger
logger = Logger.get_logger()


class ElasticCrud:

    def __init__(self, index_name=config.INDEX_NAME):
        try:
            self.es = Elasticsearch(config.ELASTIC_CONN)
            logger.info()
        except Exception as e:
            logger.error(f"Failed to connect{e}")
            self.index_name = index_name





    def create_index(self):

        if self.es.indices.exists(index=self.index_name):

            self.es.indices.delete(index=self.index_name)

        self.es.indices.create(index=self.index_name)


    def create_data(self, doc_id, doc):

        self.es.index(index=self.index_name, id=doc_id, document=doc)


