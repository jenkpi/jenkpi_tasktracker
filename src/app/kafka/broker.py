from faststream.confluent import KafkaBroker

from app.config import KafkaSettings

kafka_settings = KafkaSettings(_env_prefix="KAFKA_")
broker = KafkaBroker(kafka_settings.socket)

kafka_publisher = broker.publisher(kafka_settings.topic)
