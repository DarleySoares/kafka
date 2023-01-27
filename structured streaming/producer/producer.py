from typing import Dict, Union
from kafka import KafkaProducer
import json
import requests
import time


class Producer:

    def __init__(self, topic) -> None:

        self.kafka_broker: str = 'kafka:29092'
        self.topic: str = topic
        self.producer = KafkaProducer(
            bootstrap_servers = self.kafka_broker,
            value_serializer = lambda msg: json.dumps(msg).encode('utf-8')
        )
        
        print('Kafka Producer has been initiated...')

    def get_mensage(self) -> str:

        url: str = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.request("GET", url)
        return json.loads(response.text)["USDBRL"]
     
    def send_mensage(self, mensage: Dict[str, Union[str, int, float, bool]]) -> None:

        self.producer.send(
            self.topic,
            mensage
        )
        self.producer.flush()
    
        print(mensage)
        print('Message sent successfully...')
        
    def run(self) -> None:

        while(True):
            mensage: str = self.get_mensage()
            self.send_mensage(mensage)
            time.sleep(30) 
        

if __name__ == "__main__":
    
    time.sleep(120)
    producer = Producer('quotation_USDBRL')
    producer.run()
