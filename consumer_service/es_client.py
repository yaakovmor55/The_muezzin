from elasticsearch import Elasticsearch
import config



class ElasticCrud:

    def __init__(self, index_name=config.INDEX_NAME):
        self.es = Elasticsearch(config.ELASTIC_CONN)
        self.index_name = index_name




    def create_index(self):

        if self.es.indices.exists(index=self.index_name):

            self.es.indices.delete(index=self.index_name)
        self.es.indices.create(index=self.index_name)


    def create_data(self, doc_id, doc):

            self.es.index(index=self.index_name, id=doc_id, document=doc)


