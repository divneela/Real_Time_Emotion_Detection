# Description: Kafka producer for emotion detection stream
from json import dumps
from kafka import KafkaProducer

class Emotion_kafka_producer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
        
    def send(self,message):
        data = {'key': None, 'value': message}
        print("Sending message to Kafka producer",  data)
        self.producer.send('emotion-detection-stream', data)

