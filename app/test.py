from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pre_flight import ICEBERG_DATABASE_NAME

database_name = ICEBERG_DATABASE_NAME

spark = SparkSession.builder.getOrCreate()

df = spark.table(f"local.{database_name}.user_transaction_agg")
print(df.show())


