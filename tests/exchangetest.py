import unittest
from exchange import Exchange
from order import Order
from bot import generate_stock
from player import Trader


class ExchangeTest(unittest.TestCase):
    exchange: Exchange
    stock_list: list

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize the stocks used in the competition
        cls.stock_list = []
        for i in range(100):
            cls.stock_list.append(generate_stock(i))

    def setUp(self) -> None:
        self.exchange = Exchange("A", 2, 0.002, self.stock_list)

    def test_get_stock_price(self):
        self.assertTrue(self.exchange.get_stock_price(1) == 41.158275230082566)

    def test_get_stock_data(self):
        self.assertTrue(self.exchange.get_stock_data(1) == self.stock_list[1].get_exchange_stock("A")[
                                                           :self.exchange.day + 1])

    def test_get_name(self):
        self.assertTrue( self.exchange.get_name() == "A")

    def test_queue_order(self):
        expected_queue = [[Order(1, Trader(10000), 10, "buy"), 2]]
        self.exchange.queue_order(Order(1, Trader(10000), 10, "buy"))
        self.assertTrue(self.exchange.order_queue == expected_queue)

    def test_process_order(self):
        trader = Trader(10000)
        order = Order(1, trader, 10, "buy")
        self.exchange.process_order(order)
        self.assertTrue(trader.get_cash() == 9587.59)
        self.assertTrue(trader.get_shares_owned(1) == 10)

    def test_tick(self):
        trader = Trader(10000)
        order = Order(1, trader, 10, "buy")
        self.exchange.queue_order(order)
        for i in range(self.exchange.delay):
            self.exchange.tick()
        self.assertTrue(trader.get_cash() == 9605.35)
        self.assertTrue(trader.get_shares_owned(1) == 10)
