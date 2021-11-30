import unittest
from player import Trader


class TraderTest(unittest.TestCase):
    trader: Trader

    def setUp(self) -> None:
        self.trader = Trader(10000)

    def test_get_cash(self):
        self.assertTrue(self.trader.get_cash() == 10000)

    def test_update_cash(self):
        self.trader.update_cash(-5000)
        self.assertTrue(self.trader.get_cash() == 5000)

    def test_get_shares_owned(self):
        self.assertTrue(self.trader.get_shares_owned(1) == 0)

    def test_add_shares(self):
        self.trader.add_shares(1, 100)
        self.assertTrue(self.trader.get_shares_owned(1) == 100)

    def test_remove_shares(self):
        self.trader.add_shares(1, 100)
        self.assertTrue(self.trader.get_shares_owned(1) == 100)
        self.trader.remove_shares(1, 50)
        self.assertTrue(self.trader.get_shares_owned(1) == 50)
