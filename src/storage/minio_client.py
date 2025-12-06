from minio import Minio
import json
import pandas as pd
from datetime import datetime
import io

class MinIOClient:
    def __init__(self):
        self.client = Minio(
            'localhost:9000',
            access_key='admin',
            secret_key='password123',
            secure=False
        )
        self._ensure_buckets()
    
    def _ensure_buckets(self):
        """Cria buckets para as camadas do Data Lake"""
        buckets = ['bronze', 'silver', 'gold']
        for bucket in buckets:
            if not self.client.bucket_exists(bucket):
                self.client.make_bucket(bucket)
    
    def store_raw_data(self, data, topic):
        """Armazena dados brutos na camada Bronze"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{topic}/{timestamp}.json"
        
        json_data = json.dumps(data).encode('utf-8')
        self.client.put_object(
            'bronze', filename, 
            io.BytesIO(json_data), 
            len(json_data)
        )
    
    def store_processed_data(self, df, layer, filename):
        """Armazena dados processados nas camadas Silver/Gold"""
        csv_buffer = io.BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        
        self.client.put_object(
            layer, f"{filename}.csv",
            csv_buffer, len(csv_buffer.getvalue())
        )
    
    def read_csv(self, bucket, filename):
        """Lê arquivo CSV do MinIO"""
        response = self.client.get_object(bucket, filename)
        return pd.read_csv(io.BytesIO(response.data))
    
    def list_objects(self, bucket, prefix=''):
        """Lista objetos em um bucket"""
        return [obj.object_name for obj in self.client.list_objects(bucket, prefix=prefix)]