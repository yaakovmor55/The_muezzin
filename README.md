# The_muezzin #
## three main services, ##

1. The first service (producer_service) publishes a path and metadata about a WAV audio file in Kafka,
2.  and the second service (consumer_service) listens to Kafka, generates an ID for the metadata, transcribes the files and sends them to ElasticSearch, and stores the file itself in bits in MongoDB with the path and ID
3. A third service (data_processor) takes the text from Elasticsearch and manipulates it to check if it contains "dangerous" words - which are on an "encrypted" list.

The audio to text conversion is not performed as an additional service,
but before sending to Elasticsearch the operation is done by getting the path from Mongo,
the reason for this is to avoid calling the same service twice

###### The Docker files still need to be finalized, they are not ready to run yet. #######