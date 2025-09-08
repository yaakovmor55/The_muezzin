from kafka_consumer import consumer
from es_client import  ElasticCrud
from ID_generator import IDGenerator
from mongo_crud import MongoCRUD

es = ElasticCrud()
es.create_index()
m = MongoCRUD()
for msg in consumer:
    doc = msg.value
    doc = IDGenerator.generate(doc)
    es.create_data(doc["id"], doc["metadata"])
    m.add_file(doc["path"], doc["id"])

