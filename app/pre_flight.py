from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os

spark = SparkSession.builder.getOrCreate()

ICEBERG_DATABASE_NAME = os.getenv("ICEBERG_DATABASE_NAME", "superbase")
if not spark.catalog.databaseExists(ICEBERG_DATABASE_NAME):
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {ICEBERG_DATABASE_NAME}")
    print(f"done creating the {ICEBERG_DATABASE_NAME} Database")
else:
    print(f"database {ICEBERG_DATABASE_NAME} already exists")