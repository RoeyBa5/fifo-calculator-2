from io import BytesIO

import boto3
import pandas as pd
from pandas import DataFrame


class S3Repo:
    def __init__(self):
        self._s3 = boto3.client('s3',
                                aws_access_key_id='AKIAR4OF7R4FG7DHQPH5',
                                aws_secret_access_key='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',
                                region_name='eu-west-1')
        self._bucket = 'fifo-calculator'

    def get(self, key: str) -> DataFrame:
        with BytesIO() as f:
            self._s3.download_fileobj(Bucket=self._bucket, Key=key, Fileobj=f)
            f.seek(0)
            content = f.read()
            return pd.read_csv(BytesIO(content), sep=',')
