from calculator.pricing_client import PricingClient
from models.max_loss import MaxLoss
from models.stack import Stack

pricing_client = PricingClient()


class Calculator:
    @staticmethod
    def calc_max_loss(stack: Stack) -> MaxLoss:
        max_loss = MaxLoss(asset_symbol=stack.asset_symbol, asset_name=stack.asset_name)
        try:
            current_price = pricing_client.get_price(stack.asset_symbol)
        except:
            return max_loss
        total_amount = 0
        total_gain_loss = 0
        for transaction in reversed(stack.stack):
            total_amount += transaction.amount
            total_gain_loss += transaction.amount * (current_price - transaction.price)
            if total_gain_loss < max_loss.loss:
                max_loss.loss = total_gain_loss
                max_loss.amount = total_amount
        return max_loss
