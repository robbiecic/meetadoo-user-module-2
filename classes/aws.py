import boto3
import json


class AWS:

    def __init__(self):
        # Load config settings into self.data
        with open('config.json') as json_file:
            self.data = json.load(json_file)

        self.aws_region_name = self.data['aws_region_name']
        self.aws_access_key_id = self.data['aws_access_key_id']
        self.aws_secret_access_key = self.data['aws_secret_access_key']

    def create_ses_client():
        return boto3.client('ses', region_name=self.aws_region_name, aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def create_dynamodb_client():
        return boto3.client('dynamodb', region_name=self.aws_region_name, aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def create_dynamodb_resource():
        return boto3.resource('dynamodb', region_name=self.aws_region_name, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
