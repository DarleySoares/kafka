from pyspark.sql import SparkSession


kafka_broker: str = "kafka:29092"
topic: str = "quotation_USDBRL"

spark = (
    SparkSession
    .builder
    .appName("StreamingQuotation")
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.1')
    .getOrCreate()
)

df = (
    spark
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_broker)
    .option("subscribe", topic)
    .option("startingOffsets", "earliest")
    .load()
)
        
(
    df
    .selectExpr("CAST(key as STRING)", "CAST(value AS STRING)")
    .writeStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_broker)
    .option("topic", f"consume_{topic}")
    .option("checkpointLocation", "/app/consumer/logs/checkpoint")
    .start()
    .awaitTermination()
)