from kafka import KafkaProducer
import json
import config



producer = KafkaProducer(bootstrap_servers=[config.BOOTSTRAP_SERVERS],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))




