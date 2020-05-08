import boto3
import json
import os


class AWS:

    def __init__(self):
        self.aws_region_name = os.environ['AWS_REGION_NAME']
        self.aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        self.aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

    def create_ses_client(self):
        return boto3.client('ses', region_name=self.aws_region_name, aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def create_dynamodb_client(self):
        return boto3.client('dynamodb', region_name=self.aws_region_name, aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def create_dynamodb_resource(self):
        return boto3.resource('dynamodb', region_name=self.aws_region_name, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
