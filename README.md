# The_muezzin #
## Two main services, ##

1. The first service (producer_service) publishes a path and metadata about a WAV audio file in Kafka,
2.  and the second service (consumer_service) listens to Kafka, generates an ID for the metadata, transcribes the files and sends them to Elastic Search, and stores the file itself in bits in MongoDB with the path and ID