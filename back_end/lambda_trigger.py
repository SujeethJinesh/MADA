from __future__ import print_function
import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image
from .data_processing.data_pre_processing import getCleanData

s3_client = boto3.client('s3')


def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)

        s3_client.download_file(bucket, key, download_path)
        getCleanData(download_path)
