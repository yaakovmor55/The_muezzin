from elasticsearch import Elasticsearch
import config
from logger import Logger
logger = Logger.get_logger()

class ElasticDAL:
    def __init__(self, index_name=config.INDEX_NAME):
        try:
            self.index_name = index_name
            self.es = Elasticsearch(config.ELASTIC_CONN)
            logger.info()
        except Exception as e:
            logger.error(f"Failed to connect{e}")


    def get_document(self):
        response = self.es.search(index=self.index_name, query={"match_all": {}}, size=1000)
        return response['hits']['hits']

es = ElasticDAL()
for i in es.get_document():
    print(i["_source"]["STT"])