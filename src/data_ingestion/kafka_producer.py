from kafka import KafkaProducer
import json
import pandas as pd
import time
from datetime import datetime
import logging

class CarInventoryProducer:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.logger = logging.getLogger(__name__)
    
    def send_inventory_updates(self, csv_file):
        """Envia atualizações de estoque via Kafka"""
        df = pd.read_csv(csv_file)
        
        for _, row in df.iterrows():
            message = {
                'timestamp': datetime.now().isoformat(),
                'event_type': 'inventory_update',
                'data': row.to_dict()
            }
            
            self.producer.send('car_inventory', value=message)
            self.logger.info(f"Sent: {message['data']['id']}")
            time.sleep(0.1)
        
        self.producer.flush()
    
    def send_sales_events(self, csv_file):
        """Envia eventos de venda via Kafka"""
        df = pd.read_csv(csv_file)
        
        for _, row in df.iterrows():
            message = {
                'timestamp': datetime.now().isoformat(),
                'event_type': 'sale_completed',
                'data': row.to_dict()
            }
            
            self.producer.send('car_sales', value=message)
            time.sleep(0.2)
        
        self.producer.flush()

if __name__ == "__main__":
    producer = CarInventoryProducer()
    producer.send_inventory_updates('../../datasets/car_inventory.csv')
    producer.send_sales_events('../../datasets/sales_data.csv')