import unittest
from order import Order
from bot import generate_stock
from player import Trader
from stocks import Stock


class OrderTest(unittest.TestCase):
    buy_order: Order
    sell_order: Order
    stock: Stock
    trader: Trader

    def setUp(self) -> None:
        self.stock = generate_stock(1)
        self.trader = Trader(10000)
        self.buy_order = Order(self.stock, self.trader, 10, "buy")
        self.sell_order = Order(self.stock, self.trader, 20, "sell")

    def test_get_stock(self):
        self.assertTrue(self.buy_order.get_stock() == self.stock)
        self.assertTrue(self.sell_order.get_stock() == self.stock)

    def test_get_trader(self):
        self.assertTrue(self.buy_order.get_trader() == self.trader)
        self.assertTrue(self.sell_order.get_trader() == self.trader)

    def test_get_shares(self):
        self.assertTrue(self.buy_order.get_shares() == 10)
        self.assertTrue(self.sell_order.get_shares() == 20)

    def test_get_type(self):
        self.assertTrue(self.buy_order.get_type() == "buy")
        self.assertTrue(self.sell_order.get_type() == "sell")