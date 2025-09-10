from elasticsearch import Elasticsearch
import config
from logger import Logger
logger = Logger.get_logger()

class ElasticDAL:
    def __init__(self, index_name=config.INDEX_NAME):
        try:
            self.index_name = index_name
            self.es = Elasticsearch(config.ELASTIC_CONN)
            logger.info(f"Connected successfully to {self.index_name}")
        except Exception as e:
            logger.error(f"Failed to connect{e}")


    def get_document(self):
        id_ant_stt = {}
        response = self.es.search(index=self.index_name, query={"match_all": {}}, size=1000)
        for i in response['hits']['hits']:
            id_ant_stt[i["_id"]] = i["_source"]["STT"]
        return id_ant_stt

    def update(self, unique_id, new_field, value):
        try:
            response = self.es.update(index=self.index_name, id=unique_id, body={"doc": {new_field: value}})
            logger.info(f"info: Document  updated successfully: {response['result']}")
        except Exception as e:
            logger.error(f"Error: updating document : {e}")


