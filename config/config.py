import boto3
import pika
from config.settings import Settings

class AppInitializer:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=Settings().AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Settings().AWS_SECRET_KEY,
            region_name=Settings().REGION_NAME,
        )

        self.rabbit_connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.rabbit_channel = self.rabbit_connection.channel()

    def get_s3_client(self):
        return self.s3_client

    def get_rabbit_channel(self):
        return self.rabbit_channel
