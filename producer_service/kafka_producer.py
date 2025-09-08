from kafka import KafkaProducer
import json
import config
from logger import Logger

logger = Logger.get_logger()

try:
    producer = KafkaProducer(bootstrap_servers=[config.BOOTSTRAP_SERVERS],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    logger.info()
except Exception as e:
    logger.error(e)




