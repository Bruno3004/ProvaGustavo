from kafka import KafkaConsumer
import json
from storage.minio_client import MinIOClient
import logging

class CarDataConsumer:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.consumer = KafkaConsumer(
            'car_inventory', 'car_sales',
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='car_data_group'
        )
        self.storage = MinIOClient()
        self.logger = logging.getLogger(__name__)
    
    def consume_and_store(self):
        """Consome dados do Kafka e armazena no Data Lake"""
        for message in self.consumer:
            try:
                data = message.value
                topic = message.topic
                
                # Armazena na camada Bronze (dados brutos)
                self.storage.store_raw_data(data, topic)
                self.logger.info(f"Stored data from {topic}")
                
            except Exception as e:
                self.logger.error(f"Error processing message: {e}")

if __name__ == "__main__":
    consumer = CarDataConsumer()
    consumer.consume_and_store()