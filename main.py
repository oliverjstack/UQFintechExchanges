from bot import *
from exchange import Exchange, CentralHub
from abc import ABC, abstractmethod
from player import Trader
from numpy.random import randint
from typing import List
from order import Order

# Initialize the stocks used in the competition
stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))


class Strategy(ABC):
    order_log: dict
    current_day: int

    def __init__(self):
        self.current_day = 0
        self.order_log = dict()

    def get_order_log(self):
        return self.order_log

    def tick(self):
        self.current_day += 1

    @abstractmethod
    def strategy(self, trader: Trader, exchanges: List[Exchange]):
        pass


class RandomStrategy(Strategy):
    def strategy(self, trader: Trader, exchanges: List[Exchange]):
        exchange_choice = exchanges[randint(0, 4)]
        stock_choice = randint(0, 100)
        orders = []
        if trader.get_shares_owned(stock_choice) == 0:
            print("buying...")
            order = Order(stock_choice, trader, 1, "buy")
            orders.append((order, exchange_choice.get_name()))
        else:
            print("selling...")
            order = Order(stock_choice, trader, trader.get_shares_owned(stock_choice), "sell")
            orders.append((order, exchange_choice.get_name()))
        self.order_log[self.current_day] = [(order, exchange_choice.get_name())]
        return orders


class EnvironmentSetup(ABC):
    exchanges: List[Exchange]
    central_hub: CentralHub

    def get_exchange(self, name) -> Exchange:
        for exchange in self.exchanges:
            if exchange.get_name() == name:
                return exchange

    def get_exchanges(self) -> List[Exchange]:
        return self.exchanges

    def tick(self) -> None:
        self.central_hub.tick(self.exchanges)

    @abstractmethod
    def run(self):
        pass


class LowDelayEnvironment(EnvironmentSetup):
    def __init__(self):
        delays = dict()
        bps = dict()
        for exchange in EXCHANGES:
            delays[exchange] = 2
            bps[exchange] = 0.002

        self.central_hub = CentralHub(delays, bps)
        self.exchanges = [Exchange("A", stock_list, self.central_hub),
                          Exchange("B", stock_list, self.central_hub),
                          Exchange("C", stock_list, self.central_hub),
                          Exchange("D", stock_list, self.central_hub),
                          Exchange("E", stock_list, self.central_hub)]

    def run(self) -> None:
        trader = Trader(10000)
        strategy = RandomStrategy()
        for _ in range(STOCK_TIMELINE):
            orders = strategy.strategy(trader, self.exchanges)
            for order, exchange in orders:
                self.central_hub.queue_order(order, exchange)
            print(trader.get_cash())
            self.tick()
            strategy.tick()
        print(strategy.get_order_log())

#
# low = LowDelayEnvironment()
# low.run()

plot_stock([stock_list[0].get_main_stock(), stock_list[0].get_normal_stock(0), stock_list[0].get_normal_stock(1),
            stock_list[0].get_normal_stock(2), stock_list[0].get_epsilon_data()])
