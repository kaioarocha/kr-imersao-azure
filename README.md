# kr-imersao-azure

Provisionamento dos recursos do ambiente Azure:
- Azure Data Factory
- Azure SQL Database
- Azure Data Lake
- Linked Service
- Azure Key Vault
- Azure Databricks

#### Testes realizados 

Azure Data Factory
- Inserção de dados de planilha excel no Azure SQL Database: [`clique aqui`](pipeline/COPY_COPYDATA.json)
- Extração de dados da API do NY Times (https://developer.nytimes.com/) e armazenamento dados no Azure Data Lake: [`clique aqui`](pipeline/COPY_COPYDATAAPI.json)

- Ingestão do SQL Server Local para o Azure SQL Database .. [EM DESENVOLVIMENTO]

Databricks:
- Configuração para acesso dos containers do Data Lake [`clique aqui`](dbw-imersaoazure/Connection_Data_Lake.py)
- Configuração para acessar o Azure SQL Database [`clique aqui`](dbw-imersaoazure/Connection_DB.py)

  Notebooks de configuração de arquitetura em formato Delta .. [EM DESENVOLVIMENTO]. 

