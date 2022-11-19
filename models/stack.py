import dataclasses

from dataclasses_json import dataclass_json

from models.transaction import Transaction


@dataclass_json
@dataclasses.dataclass
class Stack:
    asset_name: str
    asset_symbol: str
    stack: [Transaction]
