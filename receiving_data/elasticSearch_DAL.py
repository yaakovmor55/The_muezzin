from elasticsearch import Elasticsearch
import config



class ElasticCrud:

    def __init__(self,data, mapping = config.CUSTOM_MAPPING, index_name = config.INDEX_NAME):
        self.es = Elasticsearch(config.ELASTIC_CONN)
        self.mapp = mapping
        self.index_name = index_name
        self.data = data



    def create_index(self):

        if self.es.indices.exists(index=self.index_name):
            self.es.indices.delete(index=self.index_name)
        self.es.indices.create(index=self.index_name, body={"mappings": self.mapp})
        print(self.es.indices.get_mapping(index=self.index_name))

    def create_data(self):
        for i, record in enumerate(self.data):
            self.es.index(index=self.index_name, document=record)



