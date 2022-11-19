import dataclasses

from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class MaxLoss:
    asset_name: str
    asset_symbol: str
    loss: float = 0
    amount: float = 0
