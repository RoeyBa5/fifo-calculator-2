import dataclasses
from datetime import datetime
from typing import List

from dataclasses_json import config
from dataclasses_json import dataclass_json
from dateutil.parser import parse


def date_encoder(obj):
    if not obj:
        return None
    return datetime.strptime(obj, "%d/%m/%Y")


def date_decoder(obj):
    if not obj:
        return None
    return parse(obj)


@dataclass_json
@dataclasses.dataclass
class PricePoint:
    date: datetime = dataclasses.field(metadata=config(encoder=date_encoder, decoder=date_decoder, field_name='D_p'))
    price: float = dataclasses.field(metadata=config(field_name='C_p'))


@dataclass_json
@dataclasses.dataclass
class PriceResponse:
    paperId: str
    paperName: str
    points: List[PricePoint]
