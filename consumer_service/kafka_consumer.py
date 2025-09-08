import json
from kafka import KafkaConsumer
import config


consumer = KafkaConsumer(
    config.PODCASTS_TOPIC,
    bootstrap_servers=[config.BOOTSTRAP_SERVERS],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

