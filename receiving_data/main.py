from kafka_consumer import consumer


for msg in consumer:
    print(msg.value)



