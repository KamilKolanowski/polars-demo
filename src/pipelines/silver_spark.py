from pyspark.sql import SparkSession

def read_sales():
    spark = SparkSession.builder \
    .appName("SimpleSparkApp") \
    .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    df = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

    return df

