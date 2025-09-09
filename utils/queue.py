import os
import json
import boto3

from config.config import AppInitializer
from utils.convert import convert_to_mp3

s3_client = AppInitializer().get_s3_client

def download_from_s3(s3_client, bucket_name, object_key, download_path):
    s3_client.download_file(bucket_name, object_key, download_path)
    print(f"Downloaded {object_key} → {download_path}")


def upload_to_s3(s3_client, bucket_name, file_path, object_key):
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f"Uploaded {file_path} → s3://{bucket_name}/{object_key}")


def callback(ch, method, properties, body):
    print(f"Received message: {body}")
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

    ch.basic_ack(delivery_tag=method.delivery_tag)

