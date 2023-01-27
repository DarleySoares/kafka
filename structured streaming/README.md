# Kafka + Structured Streaming

## Objective

## Technologies


## Architecture
   
![Architecture](./img/data_engineering.drawio.png)

## Debug

```bash
docker-compose up -d
```

```bash
docker exec -it spark-master bash
```
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /app/consumer/consumer.py
```