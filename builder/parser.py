from pandas import DataFrame

from builder.convertor import convert
from repository.s3 import S3Repo

s3 = S3Repo()


class Parser:
    @staticmethod
    def load(path: str) -> DataFrame:
        df = s3.get(path)
        df = convert(df)
        df = _filter_rows(df)
        return df


def _filter_rows(df: DataFrame) -> DataFrame:
    df = df[df['proof'] != 0]
    df = df[(df['action'] == 'buy') | (df['action'] == 'sell')]
    df = df[df['asset_symbol'] != 9992975]
    df['amount'] = df['amount'].apply(lambda x: x / 100)
    return df
