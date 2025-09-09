from kafka_consumer import consumer
from es_client import  ElasticCrud
from ID_generator import IDGenerator
from mongo_crud import MongoCRUD
from stt import AudioTranscriber
from logger import Logger
logger = Logger.get_logger()



try:
    es = ElasticCrud()
    es.create_index()
    m = MongoCRUD()
    aut = AudioTranscriber()

    for msg in consumer:
        doc = msg.value
        doc = IDGenerator.generate(doc)
        text = aut.transcribe(doc["path"])
        doc["metadata"]["STT"] = text
        print(doc)
        es.create_data(doc["id"], doc["metadata"])
        m.add_file(doc["path"], doc["id"])
        logger.info()
except Exception as e:
    logger.error(e)

