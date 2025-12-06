# KPIs e Métricas do Sistema

## KPIs Principais

### 1. Estoque
- **Total de Veículos**: Quantidade total de carros no estoque
- **Valor Total do Estoque**: Soma dos preços de todos os veículos
- **Preço Médio**: Preço médio dos veículos em estoque
- **Taxa de Disponibilidade**: % de veículos disponíveis para venda
- **Idade Média da Frota**: Idade média dos veículos em anos

### 2. Vendas
- **Total de Vendas**: Número total de vendas realizadas
- **Receita Total**: Valor total das vendas
- **Ticket Médio**: Valor médio por venda
- **Taxa de Conversão**: % de veículos vendidos vs. estoque total
- **Tempo Médio de Venda**: Dias entre entrada e venda

### 3. Análise por Marca
- **Estoque por Marca**: Quantidade de veículos por fabricante
- **Vendas por Marca**: Número de vendas por fabricante
- **Rotatividade por Marca**: Velocidade de venda por marca
- **Margem por Marca**: Diferença entre preço de entrada e venda

### 4. Análise Temporal
- **Vendas Mensais**: Evolução das vendas ao longo do tempo
- **Sazonalidade**: Padrões de venda por período
- **Entrada vs. Saída**: Comparação entre novos veículos e vendas
- **Tendências de Preço**: Evolução dos preços médios

## Dashboards Disponíveis

### Dashboard Executivo
- Visão geral dos KPIs principais
- Gráficos de tendência
- Alertas de estoque baixo
- Performance de vendedores

### Dashboard Operacional
- Estoque detalhado por modelo
- Veículos com maior tempo em estoque
- Análise de preços por categoria
- Relatório de entrada/saída diária

### Dashboard Financeiro
- Receita por período
- Análise de margem
- Projeções de faturamento
- ROI por marca/modelo

## Alertas Configurados

### Estoque
- Estoque baixo (< 5 unidades por modelo)
- Veículos parados há mais de 90 dias
- Variação de preço > 10%

### Vendas
- Meta mensal não atingida
- Queda de vendas > 20% vs. mês anterior
- Vendedor sem vendas há 7 dias

## APIs Disponíveis

### Endpoints Principais
- `GET /kpis` - KPIs principais
- `GET /inventory/by-brand` - Estoque por marca
- `GET /inventory/available` - Veículos disponíveis
- `GET /sales/summary` - Resumo de vendas
- `GET /analytics/price-distribution` - Distribuição de preços

### Exemplo de Resposta
```json
{
  "total_veiculos": 1000,
  "valor_total_estoque": 45000000.00,
  "preco_medio": 45000.00,
  "veiculos_disponiveis": 600,
  "marcas_ativas": 7,
  "idade_media_frota": 2.3
}
```