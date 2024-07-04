from pyspark.sql import SparkSession

# Inicia a sessão do Spark
spark = SparkSession.builder \
    .appName("Outro Teste") \
    .getOrCreate()

# Dados de exemplo
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3), ("Eliel", 4)]
df = spark.createDataFrame(data, ["Name", "Value"])

# Mostra o DataFrame
df.show()

# Salva o DataFrame como arquivo Parquet
df.write.mode("overwrite").parquet("/opt/spark/apps/v2/test.parquet")
