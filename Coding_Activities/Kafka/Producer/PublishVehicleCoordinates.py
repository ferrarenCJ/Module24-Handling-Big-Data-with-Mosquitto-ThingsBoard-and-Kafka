import kafka
import time
import random
import json
from time import sleep
from kafka import KafkaAdminClient

# define producer and consumer variable
sensor_data = {
    'longitude': 0,
    'latitude': 0
}

topic_name = 'vehicle-coordinates'

client = KafkaAdminClient(
    bootstrap_servers='localhost:9092'
)

producer = kafka.KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

consumer = kafka.KafkaConsumer(
    bootstrap_servers=['localhost:9092']
)


def acked(err, msg):
    if err is not None:
        print(
            "Failed to deliver message: {0}: {1}"
            .format(msg.value(), err.str())
        )
    else:
        print(
            "Message produced: {0}"
            .format(msg.value())
        )


try:

    print(f"Using topic: {topic_name}")

    consumer.close()
    client.close()

    while True:

        longitude = random.randint(-180, 180)
        latitude = random.randint(-90, 90)

        print(
            f"longitude: {longitude} latitude: {latitude}"
        )

        sensor_data['longitude'] = longitude
        sensor_data['latitude'] = latitude

        producer.send(
            topic_name,
            value=sensor_data
        )

        producer.flush()

        sleep(3)

except KeyboardInterrupt:
    pass

producer.close()