from config.settings import Settings
from config.config import AppInitializer
from utils.queue import make_callback # notice we pass s3_client into callback

def main():
    app = AppInitializer()
    s3_client = app.get_s3_client()
    channel = app.get_rabbit_channel()

    callback = make_callback(s3_client)

    channel.basic_consume(
        queue=Settings().VIDEO_QUEUE,
        on_message_callback=callback,
        auto_ack=False  
    )

    print("[INFO] Waiting for messages. Press CTRL+C to exit.")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("[INFO] Shutting down gracefully...")
        channel.stop_consuming()
        app.close()  


if __name__ == "__main__":
    main()
