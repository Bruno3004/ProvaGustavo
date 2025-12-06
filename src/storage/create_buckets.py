from minio import Minio

def create_buckets():
    """Cria os buckets necessarios no MinIO"""
    client = Minio(
        'localhost:9000',
        access_key='admin',
        secret_key='password123',
        secure=False
    )
    
    buckets = ['bronze', 'silver', 'gold']
    
    for bucket in buckets:
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
            print(f"Bucket '{bucket}' criado com sucesso!")
        else:
            print(f"Bucket '{bucket}' ja existe.")

if __name__ == "__main__":
    create_buckets()