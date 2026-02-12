from pyspark import pipelines as sdp
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
# from typing import Any

# spark: Any 
spark = SparkSession.builder.appName('abc').getOrCreate()


@sdp.materialized_view(name="userbase.user_data")
def raw_user():
    return spark.read.format("csv").option("header", True).load("/app/data/user.csv")

@sdp.materialized_view(name="userbase.transaction_data")
def raw_transaction():
    return spark.read.format("csv").option("header", True).load("/app/data/user_transaction.csv")

# @sdp.materialized_view(name="idowubase.clean_data")
# def clean_data():
#     return spark.table("local.idowubase.raw_data").withColumnRenamed("id","user_id")


@sdp.materialized_view(name="userbase.user_transaction_joined_data")
def join_user_transaction_data():
    df_user = spark.table("local.userbase.user_data")
    df_transaction_data = spark.table("local.userbase.transaction_data")
    df_joined = df_user.join(df_transaction_data, "user_id")
    return df_joined 
    

# df = spark.table("local.userbase.user_transaction_joined_data")
# df = df.groupBy("user_id").agg(F.count("user_id").alias("transaction_count"))
@sdp.materialized_view(name="userbase.user_transaction_agg")
def user_transaction_agg():
    df = spark.table("local.userbase.user_transaction_joined_data")
    df_group = df.groupBy("user_id").agg(F.count("user_id").alias("transaction_count"))
    return df_group


# @sdp.append_flow(name="idowubase.data_user_joines")
# def join_user_data_new():
#     return spark.table("local.idowubase.clean_data").join(spark.table("local.idowubase.user_data"),"user_id")


# id,name,age,country,signup_date