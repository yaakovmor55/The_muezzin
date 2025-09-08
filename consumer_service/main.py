from kafka_consumer import consumer
from es_client import  ElasticCrud
from ID_generator import IDGenerator

es = ElasticCrud()
es.create_index()
for msg in consumer:
    doc = msg.value
    doc = IDGenerator.generate(doc)
    es.create_data(doc["id"], doc["metadata"])
    # print(doc)




