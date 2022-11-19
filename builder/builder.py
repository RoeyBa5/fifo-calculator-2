from typing import Dict

import botocore.exceptions
from pandas import Series

from builder.parser import Parser
from models.stack import Stack
from models.transaction import Transaction, Action


class StackBuilder:
    @staticmethod
    def build(path: str) -> [Stack]:
        transactions = StackBuilder._load(path)
        return StackBuilder._build_stacks(transactions)

    @staticmethod
    def _load(path: str) -> [Transaction]:
        transactions = []
        for file in range(1, 20):
            try:
                df = Parser.load(f'{path}/{file}.csv')
            except botocore.exceptions.ClientError:
                break
            transactions.extend([_build_transaction(row) for _, row in df.iterrows()])
        transactions.sort(key=lambda x: x.date)
        return transactions

    @staticmethod
    def _build_stacks(transactions: [Transaction]) -> Dict[str, Stack]:
        assets_symbols = set([t.asset_symbol for t in transactions])
        stacks = dict()
        for symbol in assets_symbols:
            asset_transactions = [t for t in transactions if t.asset_symbol == symbol]
            try:
                stacks[symbol] = Stack(asset_name=asset_transactions[0].asset_name, asset_symbol=symbol,
                                       stack=_add_transactions(asset_transactions))
            except ValueError:
                pass
        return stacks


def _build_transaction(row: Series) -> Transaction:
    return Transaction(
        date=row['date'].to_pydatetime(),
        asset_name=row['asset_name'],
        asset_symbol=row['asset_symbol'],
        action=Action(row['action']),
        amount=row['amount'],
        price=row['price']
    )


def _add_transactions(asset_transactions: [Transaction]) -> [Transaction]:
    stack = []
    for transaction in asset_transactions:
        if transaction.action == Action.BUY:
            stack.append(transaction)
        elif transaction.action == Action.SELL:
            stack = _sell(stack, transaction)
    return stack


def _sell(stack: [Transaction], transaction: Transaction) -> [Transaction]:
    amount = transaction.amount
    for i, t in enumerate(stack):
        if t.amount > amount:
            t.amount -= amount
            return [transaction for transaction in stack if transaction is not None]
        elif t.amount == amount:
            stack.pop(i)
            return [transaction for transaction in stack if transaction is not None]
        else:
            amount -= t.amount
            stack[i] = None
    raise ValueError('Not enough assets to sell')
