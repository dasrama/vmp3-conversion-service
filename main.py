from config.settings import Settings
from config.config import AppInitializer
from utils.queue import callback

def main():
    app = AppInitializer()
    s3_client = app.get_s3_client()
    channel = app.get_rabbit_channel()

    channel.basic_consume(
        queue=Settings().QUEUE,
        on_message_callback=callback
    )
    