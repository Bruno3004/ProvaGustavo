from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import sys
import os

# Adicionar path do projeto
sys.path.append('/opt/airflow/dags/src')

from data_processing.spark_processor import CarDataProcessor
from storage.minio_client import MinIOClient

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'car_inventory_etl',
    default_args=default_args,
    description='ETL pipeline para dados de estoque de carros',
    schedule_interval='@daily',
    catchup=False,
    tags=['car-inventory', 'etl']
)

def extract_data():
    """Extrai dados de fontes externas"""
    print("Extraindo dados...")
    # Simula extração de API externa ou banco de dados
    return "Dados extraídos com sucesso"

def process_inventory_data():
    """Processa dados de estoque"""
    processor = CarDataProcessor()
    processor.process_inventory_data()
    return "Dados de estoque processados"

def calculate_daily_kpis():
    """Calcula KPIs diários"""
    processor = CarDataProcessor()
    kpis = processor.calculate_kpis()
    print(f"KPIs calculados: {kpis}")
    return "KPIs calculados com sucesso"

def create_analytics_tables():
    """Cria tabelas analíticas"""
    processor = CarDataProcessor()
    processor.create_analytics_tables()
    return "Tabelas analíticas criadas"

# Definir tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_inventory',
    python_callable=process_inventory_data,
    dag=dag
)

kpis_task = PythonOperator(
    task_id='calculate_kpis',
    python_callable=calculate_daily_kpis,
    dag=dag
)

analytics_task = PythonOperator(
    task_id='create_analytics',
    python_callable=create_analytics_tables,
    dag=dag
)

# Definir dependências
extract_task >> process_task >> [kpis_task, analytics_task]