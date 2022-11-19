import pandas as pd
from pandas import DataFrame

month_conversion = {
    'בינו׳': '01',
    'בפבר׳': '02',
    'במרץ': '03',
    'באפר׳': '04',
    'במאי': '05',
    'ביוני': '06',
    'ביולי': '07',
    'באוג׳': '08',
    'בספט׳': '09',
    'באוק׳': '10',
    'בנוב׳': '11',
    'בדצמ׳': '12'
}


def convert(df: DataFrame) -> DataFrame:
    df.columns = ['date', 'asset_name', 'asset_symbol', 'action', 'amount', 'price', 'credit', 'debit', 'fee',
                  'balance', 'proof']
    df.drop(columns=['credit', 'debit', 'fee'], inplace=True)
    df['date'] = df['date'].apply(lambda x: _convert_date(x))
    df['date'] = pd.to_datetime(df['date'], format='%d %m %Y')
    df['action'] = df['action'].apply(lambda x: x.replace('קניה', 'buy').replace('מכירה', 'sell'))
    df['amount'] = df['amount'].astype(float)
    df['price'] = df['price'].astype(float)
    df['balance'] = df['balance'].astype(float)
    return df


def _convert_date(date: str) -> str:
    new_date = date.split(' ')
    new_date[0] = new_date[0].zfill(2)
    new_date[1] = month_conversion[new_date[1]]
    return ' '.join(new_date)
