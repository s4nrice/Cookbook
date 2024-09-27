import os

import boto3
from botocore.client import Config


class YandexStorage:

    access_key_id = os.environ.get('ACCESS_KEY_ID')
    secret_access_key = os.environ.get('SECRET_ACCESS_KEY')
    bucket_name = os.environ.get('BUCKET_NAME')
    endpoint_url = os.environ.get('ENDPOINT_URL')

    @classmethod
    def create_s3_client(cls):
        session = boto3.session.Session()
        s3_client = session.client(
            service_name='s3',
            aws_access_key_id=cls.access_key_id,
            aws_secret_access_key=cls.secret_access_key,
            endpoint_url=cls.endpoint_url,
            config=Config(signature_version='s3v4')
        )
        return s3_client

    def download_file(s3_client, object_name, file_path):
        s3_client.download_file(bucket_name, object_name, file_path)