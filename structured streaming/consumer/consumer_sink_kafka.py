from pyspark.sql import SparkSession
from pyspark.sql.functions import col, encode, from_json, lit, struct, to_json
from pyspark.sql.streaming import DataStreamReader
from pyspark.sql.types import StructType, StructField, StringType, TimestampType


kafka_broker: str = "kafka:29092"
topic: str = "quotation_USDBRL"

spark = (
    SparkSession
    .builder
    .appName("StreamingQuotation")
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.1')
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

df: DataStreamReader = (
    spark
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_broker)
    .option("subscribe", topic)
    .option("startingOffsets", "earliest")
    .load()
)

schema = StructType([
    StructField("code", StringType(), True),
    StructField("codein", StringType(), True),
    StructField("name", StringType(), True),
    StructField("high", StringType(), True),
    StructField("low", StringType(), True),
    StructField("varBid", StringType(), True),
    StructField("pctChange", StringType(), True),
    StructField("bid", StringType(), True),
    StructField("ask", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("create_date", TimestampType(), True),
])

df = (
    df
    .selectExpr("CAST(key as STRING)", "CAST(value AS STRING)")
    .withColumn("value", from_json(col("value"), schema))
    .select("value.*")
)

df = (
    df
    .withColumn("high", col("high").cast("double"))
    .withColumn("low", col("low").cast("double"))
    .withColumn("varBid", col("varBid").cast("double"))
    .withColumn("pctChange", col("pctChange").cast("double"))
    .withColumn("bid", col("bid").cast("double"))
    .withColumn("ask", col("ask").cast("double"))
    .select(
        "code",
        "codein",
        "high",
        "low",
        "varBid",
        "pctChange",
        "bid",
        "ask",
        "create_date"
    )
)

df = (
    df
    .withColumn("key", lit("key"))
    .withColumn("value", to_json(struct(col("*"))))
    .withColumn("key", encode(col("key"), "iso-8859-1").cast("binary"))
    .withColumn("value", encode(col("value"), "iso-8859-1").cast("binary"))
)

(
    df
    .writeStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_broker)
    .option("topic", f"consume_{topic}")
    .option("checkpointLocation", "/app/consumer/logs/checkpoint")
    .start()
    .awaitTermination()
)
