import pandas as pd
from storage.minio_client import MinIOClient

class CarDataProcessor:
    def __init__(self):
        self.storage = MinIOClient()
    
    def process_inventory_data(self):
        """Processa dados de estoque - Camada Silver"""
        # Lê dados da camada Bronze
        df = pd.read_csv('../datasets/car_inventory.csv')
        
        # Transformações
        df['preco_categoria'] = pd.cut(df['preco'], 
                                     bins=[0, 30000, 50000, float('inf')], 
                                     labels=['Econômico', 'Médio', 'Premium'])
        
        df['idade_veiculo'] = 2024 - df['ano']
        df['km_por_ano'] = df['quilometragem'] / (df['idade_veiculo'] + 1)
        
        # Armazena na camada Silver
        self.storage.store_processed_data(df, 'silver', 'inventory_processed')
        return df
    
    def create_analytics_tables(self):
        """Cria tabelas analíticas - Camada Gold"""
        df = pd.read_csv('../datasets/car_inventory.csv')
        sales_df = pd.read_csv('../datasets/sales_data.csv')
        
        # KPI: Estoque por marca
        estoque_marca = df.groupby('marca').agg({
            'id': 'count',
            'preco': 'mean'
        }).rename(columns={'id': 'quantidade', 'preco': 'preco_medio'})
        
        # KPI: Rotatividade
        vendas_marca = sales_df.merge(df, left_on='car_id', right_on='id')
        rotatividade = vendas_marca.groupby('marca').size().reset_index(name='vendas')
        
        # KPI: Análise temporal
        df['data_entrada'] = pd.to_datetime(df['data_entrada'])
        entrada_mensal = df.groupby(df['data_entrada'].dt.to_period('M')).size()
        
        # Armazena na camada Gold
        self.storage.store_processed_data(estoque_marca.reset_index(), 'gold', 'kpi_estoque_marca')
        self.storage.store_processed_data(rotatividade, 'gold', 'kpi_rotatividade')
        
        return {
            'estoque_marca': estoque_marca,
            'rotatividade': rotatividade,
            'entrada_mensal': entrada_mensal
        }
    
    def calculate_kpis(self):
        """Calcula KPIs principais"""
        df = pd.read_csv('../datasets/car_inventory.csv')
        
        kpis = {
            'total_veiculos': len(df),
            'valor_total_estoque': df['preco'].sum(),
            'preco_medio': df['preco'].mean(),
            'veiculos_disponiveis': len(df[df['status'] == 'Disponível']),
            'marcas_ativas': df['marca'].nunique(),
            'idade_media_frota': (2024 - df['ano']).mean()
        }
        
        kpis_df = pd.DataFrame([kpis])
        self.storage.store_processed_data(kpis_df, 'gold', 'kpis_principais')
        
        return kpis

if __name__ == "__main__":
    processor = CarDataProcessor()
    processor.process_inventory_data()
    processor.create_analytics_tables()
    kpis = processor.calculate_kpis()
    print("KPIs calculados:", kpis)