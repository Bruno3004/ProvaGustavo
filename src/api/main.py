from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from storage.minio_client import MinIOClient
from data_processing.spark_processor import CarDataProcessor
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="Car Inventory API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

storage = MinIOClient()
processor = CarDataProcessor()

@app.get("/")
def read_root():
    return {"message": "Car Inventory Management API"}

@app.get("/kpis")
def get_kpis():
    """Retorna KPIs principais"""
    try:
        kpis = processor.calculate_kpis()
        return kpis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/inventory/by-brand")
def get_inventory_by_brand():
    """Retorna estoque agrupado por marca"""
    try:
        df = pd.read_csv('../../datasets/car_inventory.csv')
        result = df.groupby('marca').agg({
            'id': 'count',
            'preco': 'mean'
        }).rename(columns={'id': 'quantidade', 'preco': 'preco_medio'})
        return result.to_dict('index')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/inventory/available")
def get_available_inventory():
    """Retorna veículos disponíveis"""
    try:
        df = pd.read_csv('../../datasets/car_inventory.csv')
        available = df[df['status'] == 'Disponível']
        return available.to_dict('records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/sales/summary")
def get_sales_summary():
    """Retorna resumo de vendas"""
    try:
        df = pd.read_csv('../../datasets/sales_data.csv')
        summary = {
            'total_vendas': len(df),
            'valor_total': df['preco_venda'].sum(),
            'ticket_medio': df['preco_venda'].mean(),
            'vendas_por_forma_pagamento': df['forma_pagamento'].value_counts().to_dict()
        }
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analytics/price-distribution")
def get_price_distribution():
    """Retorna distribuição de preços"""
    try:
        df = pd.read_csv('../../datasets/car_inventory.csv')
        bins = [0, 30000, 50000, 80000, float('inf')]
        labels = ['Até 30k', '30k-50k', '50k-80k', 'Acima 80k']
        df['faixa_preco'] = pd.cut(df['preco'], bins=bins, labels=labels)
        distribution = df['faixa_preco'].value_counts().to_dict()
        return distribution
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)