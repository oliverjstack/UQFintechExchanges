import unittest
from stocks import Stock
from bot import generate_stock


class StockTest(unittest.TestCase):
    stock: Stock

    def setUp(self) -> None:
        self.stock = generate_stock(1)

    def test_get_exchange_stock(self):
        expected_values = [41.158275230082566, 41, 41.74502538233401, 40.85971272848309, 40.89548531696851]
        exchanges = ["A", "B", "C", "D", "E"]
        for exchange, value in zip(exchanges, expected_values):
            self.assertTrue(self.stock.get_exchange_stock(exchange)[0] == value)

    def test_main_stock(self):
        self.assertTrue(self.stock.get_main_stock()[0] == 41)

    def test_normal_stock(self):
        expected_values = [40.85971272848309, 41.158275230082566, 40.89548531696851]
        for i in range(3):
            self.assertTrue(self.stock.get_normal_stock(i)[0] == expected_values[i])

    def test_epsilon_data(self):
        self.assertTrue(self.stock.get_epsilon_data()[0] == 41.74502538233401)

    def test_id(self):
        self.assertTrue(self.stock.get_id() == 1)
