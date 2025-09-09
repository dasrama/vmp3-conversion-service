import boto3
from config.settings import Settings

def main():
    s3_client = boto3.client(
        aws_access_key_id=Settings().AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Settings().AWS_SECRET_KEY,
        region_name=Settings().REGION_NAME
    )