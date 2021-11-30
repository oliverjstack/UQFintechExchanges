from bot import *
from exchange import Exchange
from player import Trader
from order import Order
from abc import ABC


class EnvironmentSetup(ABC):
    exchanges: list

    def get_exchange(self, name) -> Exchange:
        for exchange in self.exchanges:
            if exchange.get_name() == name:
                return exchange


class LowDelayEnvironment(EnvironmentSetup):
    def __init__(self):
        self.exchanges = [Exchange("A", 2, 0.002),
                          Exchange("B", 2, 0.002),
                          Exchange("C", 2, 0.002),
                          Exchange("D", 2, 0.002),
                          Exchange("E", 2, 0.002)]


stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))

low = LowDelayEnvironment()

test_trader_1 = Trader(10000)

test_order = Order(stock_list[1], test_trader_1, 253, "buy")

low.get_exchange("A").queue_order(test_order)
low.get_exchange("A").tick()
low.get_exchange("A").tick()

print(test_trader_1.get_cash(), test_trader_1.get_shares_owned(1))
