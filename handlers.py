from typing import List

from fastapi import APIRouter

from builder.builder import StackBuilder
from calculator.calculator import Calculator
from models.max_loss import MaxLoss

fifo = APIRouter()


@fifo.get('/max-loss', response_model=List[MaxLoss])
async def get_max_loss(id: str) -> List[MaxLoss]:
    stacks = StackBuilder.build(id)
    response = []
    for stack in stacks.values():
        response.append(Calculator.calc_max_loss(stack))
    return response
