from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Outro Test") \
    .getOrCreate()

data = [("Alice", 1), ("Bob", 2), ("Cathy", 3), ("Eliel", 4)]
df = spark.createDataFrame(data, ["Name", "Value"])

df.show()