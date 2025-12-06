# Arquitetura do Sistema

## Visão Geral
Sistema de análise de dados para gerenciamento de estoque de loja de carros, implementando arquitetura de Data Lake com processamento em tempo real e batch.

## Componentes

### 1. Ingestão de Dados
- **Kafka**: Streaming de dados em tempo real
  - Tópicos: `car_inventory`, `car_sales`
  - Producer: Envia atualizações de estoque e vendas
  - Consumer: Processa e armazena no Data Lake

- **Airflow**: Processamento batch (agendado)
  - DAGs para ETL diário
  - Integração com APIs externas
  - Monitoramento de pipeline

### 2. Processamento
- **Apache Spark**: Processamento distribuído
  - Transformações de dados
  - Agregações e cálculos de KPIs
  - Machine Learning (previsão de demanda)

- **Pandas**: Processamento local
  - Análises exploratórias
  - Transformações simples
  - Validação de dados

### 3. Armazenamento (Data Lake)
- **MinIO**: Storage compatível com S3
  - **Bronze**: Dados brutos (JSON)
  - **Silver**: Dados limpos e estruturados (Parquet)
  - **Gold**: Dados agregados e KPIs (Parquet)

### 4. Visualização
- **Metabase**: Dashboards e relatórios
  - KPIs em tempo real
  - Análises de tendências
  - Relatórios executivos

- **API FastAPI**: Endpoints para dados
  - REST API para aplicações
  - Documentação automática
  - Autenticação JWT

## Fluxo de Dados

```
Dados Fonte → Kafka → Consumer → MinIO (Bronze)
                                     ↓
                              Spark Processing
                                     ↓
                           MinIO (Silver/Gold)
                                     ↓
                           API + Metabase
```

## Tecnologias Utilizadas
- **Streaming**: Apache Kafka
- **Processamento**: Apache Spark, Pandas
- **Storage**: MinIO (S3-compatible)
- **Orquestração**: Docker Compose
- **API**: FastAPI
- **Visualização**: Metabase
- **Linguagem**: Python 3.8+