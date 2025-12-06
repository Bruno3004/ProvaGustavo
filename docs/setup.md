# Guia de Instalação e Configuração

## Pré-requisitos
- Docker e Docker Compose
- Python 3.8+
- Git

## Instalação

### 1. Clone o Repositório
```bash
git clone <repository-url>
cd ProvaGustavo
```

### 2. Configurar Ambiente Python
```bash
cd src
pip install -r requirements.txt
```

### 3. Subir Infraestrutura
```bash
cd infra
docker-compose up -d
```

### 4. Aguardar Inicialização
Aguarde todos os serviços subirem (aproximadamente 2-3 minutos).

### 5. Gerar Dados de Exemplo
```bash
cd datasets
python sample_data.py
```

### 6. Executar Pipeline
```bash
cd src
python main.py
```

### 7. Iniciar API
```bash
cd src/api
python main.py
```

## Verificação da Instalação

### Serviços Disponíveis
- **MinIO Console**: http://localhost:9001
  - User: admin
  - Password: password123

- **Metabase**: http://localhost:3000
  - Configurar na primeira execução

- **API**: http://localhost:8000
  - Documentação: http://localhost:8000/docs

- **Kafka**: localhost:9092
- **Spark Master**: http://localhost:8080

### Comandos Úteis
```bash
# Ver logs dos containers
docker-compose logs -f

# Parar todos os serviços
docker-compose down

# Reiniciar um serviço específico
docker-compose restart metabase

# Limpar volumes (CUIDADO: apaga dados)
docker-compose down -v
```

## Configuração do Metabase

1. Acesse http://localhost:3000
2. Configure usuário administrador
3. Conecte ao PostgreSQL:
   - Host: postgres
   - Port: 5432
   - Database: metabase
   - User: metabase
   - Password: password123

## Troubleshooting

### Problema: Porta já em uso
```bash
# Verificar portas em uso
netstat -tulpn | grep :9000

# Parar processo específico
sudo kill -9 <PID>
```

### Problema: Containers não sobem
```bash
# Verificar logs
docker-compose logs

# Recriar containers
docker-compose down
docker-compose up -d --force-recreate
```

### Problema: Dados não aparecem
1. Verificar se os dados foram gerados: `ls datasets/`
2. Executar pipeline novamente: `python src/main.py`
3. Verificar logs do MinIO