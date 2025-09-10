import os
import json

from utils.convert import convert_to_mp3


def download_from_s3(s3_client, bucket_name, object_key, download_path):
    s3_client.download_file(bucket_name, object_key, download_path)
    print(f"Downloaded {object_key} → {download_path}")


def upload_to_s3(s3_client, bucket_name, file_path, object_key):
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f"Uploaded {file_path} → s3://{bucket_name}/{object_key}")


def make_callback(s3_client):
    def callback(ch, method, properties, body):
        print(f"[INFO] Received message: {body}")

        message = json.loads(body)
        bucket_name = message["bucket"]
        video_key = message["video_key"]

        download_path = f"/tmp/{os.path.basename(video_key)}"
        output_path = download_path.rsplit(".", 1)[0] + ".mp3"

        # Download → Convert → Upload
        download_from_s3(s3_client, bucket_name, video_key, download_path)
        convert_to_mp3(download_path, output_path)
        mp3_key = video_key.rsplit(".", 1)[0] + ".mp3"
        upload_to_s3(s3_client, bucket_name, output_path, mp3_key)

        # Acknowledge message only after processing
        ch.basic_ack(delivery_tag=method.delivery_tag)

    return callback
