import pandas as pd
import psycopg2
from psycopg2 import sql

def load_data_to_postgres():
    """Carrega dados processados no PostgreSQL para visualizacao no Metabase"""
    
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='cardata',
        user='admin',
        password='password123'
    )
    
    cursor = conn.cursor()
    
    # Ler dados
    inventory_df = pd.read_csv('../../datasets/car_inventory.csv')
    sales_df = pd.read_csv('../../datasets/sales_data.csv')
    
    # Criar tabelas
    cursor.execute("""
        DROP TABLE IF EXISTS car_inventory;
        CREATE TABLE car_inventory (
            id VARCHAR(50) PRIMARY KEY,
            marca VARCHAR(50),
            modelo VARCHAR(50),
            ano INTEGER,
            cor VARCHAR(30),
            preco DECIMAL(10,2),
            quilometragem INTEGER,
            status VARCHAR(30),
            data_entrada DATE,
            vendedor_id VARCHAR(20),
            categoria VARCHAR(30)
        );
    """)
    
    cursor.execute("""
        DROP TABLE IF EXISTS sales_data;
        CREATE TABLE sales_data (
            venda_id VARCHAR(50) PRIMARY KEY,
            car_id VARCHAR(50),
            data_venda DATE,
            preco_venda DECIMAL(10,2),
            vendedor_id VARCHAR(20),
            cliente_id VARCHAR(20),
            forma_pagamento VARCHAR(30)
        );
    """)
    
    conn.commit()
    
    # Inserir dados
    for _, row in inventory_df.iterrows():
        cursor.execute("""
            INSERT INTO car_inventory VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))
    
    for _, row in sales_df.iterrows():
        cursor.execute("""
            INSERT INTO sales_data VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print("Dados carregados no PostgreSQL com sucesso!")

if __name__ == "__main__":
    load_data_to_postgres()