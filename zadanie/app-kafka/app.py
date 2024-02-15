from kafka import KafkaConsumer, KafkaProducer
import json
import logging

logger = logging.getLogger()
consumer = KafkaConsumer("zadania", bootstrap_servers=["kafka:9092"])
producer = KafkaProducer(bootstrap_servers=["kafka:9092"])

for message in consumer:
    try:
        maze_data = json.loads(message.value.decode("utf-8"))
        logger.info(f"Otrzymano wiadomość: {maze_data}")

        # Oblicz najkrótszą trasę w labiryncie
        # ...

        producer.send("rozwiazania", json.dumps({"maze_data": maze_data}).encode("utf-8"))

    except Exception as e:
        logger.error(f"Wystąpił błąd: {e}")


def konfiguracja_logowania():
    logging.basicConfig(level=logging.DEBUG)
    
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

konfiguracja_logowania()
