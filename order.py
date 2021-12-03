from player import Trader
from stocks import Stock


class Order:
    stock: int
    trader: Trader
    shares: int
    order_type: str

    def __init__(self, stock, trader, shares, order_type):
        self.stock = stock
        self.trader = trader
        self.shares = shares
        self.order_type = order_type

    def get_stock(self):
        return self.stock

    def get_trader(self):
        return self.trader

    def get_shares(self):
        return self.shares

    def get_type(self):
        return self.order_type

    def __repr__(self):
        return f"Order: {self.get_type()}:{self.get_shares()}:stock({self.get_stock()})"

    def __eq__(self, other):
        return self.trader == other.trader and \
               self.order_type == other.order_type and \
               self.stock == other.stock and \
               self.shares == other.shares
