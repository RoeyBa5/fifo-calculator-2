import dataclasses
from datetime import datetime
from enum import Enum

from dataclasses_json import dataclass_json


class Action(Enum):
    BUY = 'buy'
    SELL = 'sell'


@dataclass_json
@dataclasses.dataclass
class Transaction:
    date: datetime
    asset_name: str
    asset_symbol: str
    action: Action
    amount: float
    price: float
