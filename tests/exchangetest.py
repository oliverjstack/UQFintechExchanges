import unittest
from exchange import Exchange
from order import Order
from bot import generate_stock
from player import Trader


class ExchangeTest(unittest.TestCase):
    exchange: Exchange

    def setUp(self) -> None:
        self.exchange = Exchange("A", 2, 0.002)

    def test_get_stock(self):
        stock = generate_stock(1)
        self.assertTrue(self.exchange.get_stock(stock)[0] == 41.158275230082566)

    def test_get_name(self):
        self.assertTrue( self.exchange.get_name() == "A")

    def test_queue_order(self):
        expected_queue = [[Order(generate_stock(1), Trader(10000), 10, "buy"), 2]]
        self.exchange.queue_order(Order(generate_stock(1), Trader(10000), 10, "buy"))
        self.assertTrue(self.exchange.order_queue == expected_queue)

    def test_get_queued_orders(self):
        expected_queue = [[Order(generate_stock(1), Trader(10000), 10, "buy"), 2]]
        self.exchange.queue_order(Order(generate_stock(1), Trader(10000), 10, "buy"))
        self.assertTrue(self.exchange.get_queued_orders() == expected_queue)

    def test_process_order(self):
        trader = Trader(10000)
        order = Order(generate_stock(1), trader, 10, "buy")
        self.exchange.process_order(order)
        self.assertTrue(trader.get_cash() == 9587.59)
        self.assertTrue(trader.get_shares_owned(1) == 10)

    def test_tick(self):
        trader = Trader(10000)
        order = Order(generate_stock(1), trader, 10, "buy")
        self.exchange.queue_order(order)
        for i in range(self.exchange.delay):
            self.exchange.tick()
        self.assertTrue(trader.get_cash() == 9605.35)
        self.assertTrue(trader.get_shares_owned(1) == 10)
