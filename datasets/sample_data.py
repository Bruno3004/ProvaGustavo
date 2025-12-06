import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

def generate_car_inventory_data():
    """Gera dados de exemplo para estoque de carros"""
    
    brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen', 'Hyundai', 'Nissan']
    models = {
        'Toyota': ['Corolla', 'Camry', 'RAV4', 'Prius'],
        'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot'],
        'Ford': ['Focus', 'Fusion', 'Escape', 'F-150'],
        'Chevrolet': ['Cruze', 'Malibu', 'Equinox', 'Silverado'],
        'Volkswagen': ['Jetta', 'Passat', 'Tiguan', 'Atlas'],
        'Hyundai': ['Elantra', 'Sonata', 'Tucson', 'Santa Fe'],
        'Nissan': ['Sentra', 'Altima', 'Rogue', 'Pathfinder']
    }
    
    colors = ['Branco', 'Preto', 'Prata', 'Azul', 'Vermelho', 'Cinza']
    years = list(range(2020, 2025))
    
    data = []
    for i in range(1000):
        brand = np.random.choice(brands)
        model = np.random.choice(models[brand])
        
        record = {
            'id': f'CAR{i+1:04d}',
            'marca': brand,
            'modelo': model,
            'ano': np.random.choice(years),
            'cor': np.random.choice(colors),
            'preco': np.random.randint(25000, 80000),
            'quilometragem': np.random.randint(0, 100000),
            'status': np.random.choice(['Disponível', 'Vendido', 'Reservado'], p=[0.6, 0.3, 0.1]),
            'data_entrada': (datetime.now() - timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%d'),
            'vendedor_id': f'VEND{np.random.randint(1, 11):02d}',
            'categoria': np.random.choice(['Sedan', 'SUV', 'Hatchback', 'Pickup'])
        }
        data.append(record)
    
    df = pd.DataFrame(data)
    df.to_csv('car_inventory.csv', index=False)
    
    # Dados de vendas
    sales_data = []
    sold_cars = df[df['status'] == 'Vendido'].sample(200)
    
    for _, car in sold_cars.iterrows():
        sale = {
            'venda_id': f'SALE{len(sales_data)+1:04d}',
            'car_id': car['id'],
            'data_venda': (datetime.now() - timedelta(days=np.random.randint(1, 180))).strftime('%Y-%m-%d'),
            'preco_venda': car['preco'] * np.random.uniform(0.9, 1.1),
            'vendedor_id': car['vendedor_id'],
            'cliente_id': f'CLI{np.random.randint(1, 501):03d}',
            'forma_pagamento': np.random.choice(['À vista', 'Financiado', 'Consórcio'])
        }
        sales_data.append(sale)
    
    pd.DataFrame(sales_data).to_csv('sales_data.csv', index=False)
    print("Dados de exemplo gerados: car_inventory.csv e sales_data.csv")

if __name__ == "__main__":
    generate_car_inventory_data()