#!/usr/bin/env python3
"""
Pipeline principal do sistema de gerenciamento de estoque
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_processing.spark_processor import CarDataProcessor
from storage.minio_client import MinIOClient
import pandas as pd

def run_pipeline():
    """Executa o pipeline completo de dados"""
    print("Iniciando pipeline de dados...")
    
    # 1. Gerar dados de exemplo
    print("Gerando dados de exemplo...")
    os.system('cd ../datasets && python sample_data.py')
    
    # 2. Inicializar componentes
    processor = CarDataProcessor()
    
    # 3. Processar dados
    print("Processando dados de estoque...")
    processor.process_inventory_data()
    
    # 4. Criar tabelas analíticas
    print("Criando tabelas analiticas...")
    analytics = processor.create_analytics_tables()
    
    # 5. Calcular KPIs
    print("Calculando KPIs...")
    kpis = processor.calculate_kpis()
    
    print("\nPipeline executado com sucesso!")
    print("KPIs principais:")
    for key, value in kpis.items():
        print(f"  - {key}: {value:,.2f}" if isinstance(value, (int, float)) else f"  - {key}: {value}")
    
    print("\nPara acessar:")
    print("  - API: http://localhost:8000")
    print("  - Metabase: http://localhost:3000")
    print("  - MinIO: http://localhost:9001")

if __name__ == "__main__":
    run_pipeline()