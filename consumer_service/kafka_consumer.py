import json
from kafka import KafkaConsumer
import config
from logger import Logger
logger = Logger.get_logger()

# Contains an instance of Consumer
try:

    consumer = KafkaConsumer(
        config.PODCASTS_TOPIC,
        bootstrap_servers=[config.BOOTSTRAP_SERVERS],
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )
    logger.info("Connected successfully")
except Exception as e:
    logger.error(f"Failed to connect to listener{e}")

