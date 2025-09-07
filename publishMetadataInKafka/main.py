from publishMetadataInKafka import config
from publishMetadataInKafka.export_metadata import ExportMetadata
from publishMetadataInKafka.file_reader import ReadPath
from kafka_producer import producer


r = ReadPath()
for file in r.files_and_dirs:
    e = ExportMetadata(f"{r.path}/{file}")
    producer.send(config.PODCASTS_TOPIC,e.get_meta_data())
producer.flush()


