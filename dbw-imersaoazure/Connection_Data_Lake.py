# Databricks notebook source
# DBTITLE 1,Estabelecendo conexão com o data lake
storage_account_name = "dlsimersaoazure"

config = {f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net":dbutils.secrets.get(scope = "scopedbwimersaoazure", key = "secret-key-datalake")}

# COMMAND ----------

# DBTITLE 1,Lista de containers
containers = ["bronze", "silver", "gold"]

# COMMAND ----------

# DBTITLE 1,Criar ponto de montagem nas camadas
def mount_datalake(containers):
    try:
        for container in containers:
            dbutils.fs.mount(
                source = f"wasbs://{container}@dlsimersaoazure.blob.core.windows.net",
                mount_point = f"/mnt/{container}",
                extra_configs = config
            )
            print(container)
    except ValueError as err:
        print(err)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/

# COMMAND ----------

# DBTITLE 1,Desmonta camadas do DBFS - Alerta (Apaga camadas)
def unmount_datalake(containers):
    try:
        for container in containers:
            dbutils.fs.unmount(f"/mnt/{container}/")
    except ValueError as err:
        print(err)

# COMMAND ----------

mount_datalake(containers)

# COMMAND ----------

unmount_datalake(containers)

# COMMAND ----------

# DBTITLE 1,Lista camadas - DBFS
dbutils.fs.ls("/mnt/bronze/")
