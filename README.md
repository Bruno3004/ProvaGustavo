# Sistema de Gerenciamento de Estoque - Loja de Carros

## Visão Geral
Sistema completo de análise de dados para gerenciamento de estoque de uma loja de carros, implementando pipeline de dados com ingestão, processamento, armazenamento e visualização.

## Arquitetura
- **Ingestão**: Kafka para streaming + Airflow para batch
- **Processamento**: Apache Spark + Pandas
- **Armazenamento**: MinIO (Data Lake) com camadas Bronze/Silver/Gold
- **Visualização**: Metabase + API FastAPI
- **Orquestração**: Docker Compose

## Estrutura do Projeto
```
/docs          - Documentação completa
/src           - Scripts e código-fonte
/infra         - Docker Compose e configurações
/notebooks     - Análise exploratória
/datasets      - Dados de teste
```

## Execução Rápida
```bash
# 1. Subir infraestrutura
cd infra
docker-compose up -d

# 2. Executar pipeline
cd ../src
python main.py

# 3. Acessar dashboards
# Metabase: http://localhost:3000
# API: http://localhost:8000
```

## KPIs Principais
- Estoque por modelo/marca
- Rotatividade de veículos
- Análise de preços
- Previsão de demanda