from producer_service import config
from producer_service.export_metadata import ExportMetadata
from producer_service.file_reader import FileReader
from kafka_producer import producer

from logger import Logger

logger = Logger.get_logger()

try:
    r = FileReader()
    for file in r.files_and_dirs:
        e = ExportMetadata(f"{r.path}/{file}")
        producer.send(config.PODCASTS_TOPIC,e.build_json())
    producer.flush()
    producer.close()
    logger.info()
except Exception as e:
    logger.error(e)


