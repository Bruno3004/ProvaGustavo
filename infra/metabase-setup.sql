-- Configuração inicial do Metabase para conectar aos dados

-- Criar conexão com PostgreSQL (dados processados)
-- Esta configuração deve ser feita via interface web do Metabase

-- Exemplo de queries úteis para dashboards:

-- 1. KPIs Principais
SELECT 
    COUNT(*) as total_veiculos,
    SUM(preco) as valor_total_estoque,
    AVG(preco) as preco_medio,
    COUNT(CASE WHEN status = 'Disponível' THEN 1 END) as veiculos_disponiveis
FROM car_inventory;

-- 2. Estoque por Marca
SELECT 
    marca,
    COUNT(*) as quantidade,
    AVG(preco) as preco_medio,
    SUM(preco) as valor_total
FROM car_inventory
GROUP BY marca
ORDER BY quantidade DESC;

-- 3. Análise Temporal de Vendas
SELECT 
    DATE_TRUNC('month', data_venda::date) as mes,
    COUNT(*) as total_vendas,
    SUM(preco_venda) as receita_total,
    AVG(preco_venda) as ticket_medio
FROM sales_data
GROUP BY DATE_TRUNC('month', data_venda::date)
ORDER BY mes;

-- 4. Top Modelos Mais Vendidos
SELECT 
    ci.marca,
    ci.modelo,
    COUNT(*) as vendas,
    AVG(sd.preco_venda) as preco_medio_venda
FROM sales_data sd
JOIN car_inventory ci ON sd.car_id = ci.id
GROUP BY ci.marca, ci.modelo
ORDER BY vendas DESC
LIMIT 10;

-- 5. Análise de Rotatividade
SELECT 
    marca,
    COUNT(*) as estoque_total,
    COUNT(CASE WHEN status = 'Vendido' THEN 1 END) as vendidos,
    ROUND(
        COUNT(CASE WHEN status = 'Vendido' THEN 1 END) * 100.0 / COUNT(*), 2
    ) as taxa_rotatividade
FROM car_inventory
GROUP BY marca
ORDER BY taxa_rotatividade DESC;