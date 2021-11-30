from bot import *
from exchange import Exchange
from abc import ABC

# Initialize the stocks used in the competition
stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))


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


low = LowDelayEnvironment()
