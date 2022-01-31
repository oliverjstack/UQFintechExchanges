from bot import *
from exchange import Exchange
from abc import ABC, abstractmethod
from player import Trader
from numpy.random import randint
from typing import List, Dict
from order import Order

# Initialize the stocks used in the competition
stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))


class Strategy(ABC):
    """
    Abstract class of a strategy object in order to enforce functions required
    """
    order_log: dict
    current_day: int

    def __init__(self):
        """
        Creates a strategy object
        """
        self.current_day = 0
        self.order_log = dict()

    def get_order_log(self):
        """
        Returns the dictionary of orders placed by the strategy
        :return: Dictionary of orders
        """
        return self.order_log

    def tick(self):
        """
        Updates the internal time period for the strategy
        """
        self.current_day += 1

    @abstractmethod
    def run_strategy(self, trader: Trader, exchanges: List[Exchange]):
        pass


class TeamStrategy(Strategy):
    """
    Strategy for each team to alter
    """
    def run_strategy(self, trader: Trader, exchanges: List[Exchange]):
        """
        Function for teams to implement and return a list of orders
        :param trader: Team holding information
        :param exchanges: List of exchanges with up to date prices
        :return: List of orders wanting to be executed
        """
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
    """
    Environment abstract class created in order to compact different environment details
    """
    exchanges: List[Exchange]
    order_queue: Dict[str, List[list]]
    bps: dict
    delay: Dict[str, int]
    day: int

    def get_day(self):
        """
        Returns the current simulated day
        :return: Int representing the day
        """
        return self.day

    def queue_order(self, order: Order, exchange: str):
        """
        Queues orders placed by the team for a time period
        :param order: The order being placed
        :param exchange: The exchange the order is being placed on
        """
        self.order_queue[exchange].append([order, self.delay[exchange]])

    def process_order(self, order: Order, exchange: 'Exchange'):
        """
        Processes an order that has completed its delay period
        :param order: The order to be executed
        :param exchange: The exchange being used to execute the order
        """
        cash = order.get_shares() * exchange.get_stock_price(order.get_stock()) + \
               (order.get_shares() * exchange.get_stock_price(order.get_stock()) *
                self.bps[exchange.get_name()])
        if order.get_type() == "buy":
            if can_buy(order.get_trader(), cash):
                order.get_trader().update_cash(-1 * round(cash, 2))
                order.get_trader().add_shares(order.get_stock(), order.get_shares())
        else:
            order.get_trader().update_cash(round(cash, 2))
            order.get_trader().remove_shares(order.get_stock(), order.get_shares())

    def tick(self) -> None:
        """
        Updates relevant environment variables such as time periods for orders and
        executes trades that have finished their delay period
        """
        for exchange in self.exchanges:
            name = exchange.get_name()
            for order in self.order_queue[name]:
                order[1] -= 1

            remove_list = []
            for i, order in enumerate(self.order_queue[name]):
                if order[1] == 0:
                    self.process_order(order[0], exchange)
                    remove_list.append(i)

            for index in remove_list:
                self.order_queue[name].pop(index)

            exchange.tick()
        self.day += 1

    @abstractmethod
    def run(self):
        pass


class LowDelayEnvironment(EnvironmentSetup):
    """
    Represents an environment where all changes have a 2 time period delay and 0.002 BPS
    """
    def __init__(self):
        """
        Initializes a low delay environment
        """
        self.delay = dict()
        self.bps = dict()
        self.order_queue = dict()
        self.day = 0

        for exchange in EXCHANGES:
            self.delay[exchange] = 2
            self.bps[exchange] = 0.002
            self.order_queue[exchange] = []

        self.exchanges = [Exchange("A", stock_list),
                          Exchange("B", stock_list),
                          Exchange("C", stock_list),
                          Exchange("D", stock_list),
                          Exchange("E", stock_list)]

    def run(self) -> None:
        """
        Simulates the 750 trading period time frame and prints daily cash flow and final order log for entire period
        """
        trader = Trader(100000)
        strategy = TeamStrategy()
        for _ in range(STOCK_TIMELINE):
            # runs a strategy that choose stocks at random
            orders = strategy.run_strategy(trader, self.exchanges)
            for order, exchange in orders:
                self.queue_order(order, exchange)
            print(trader.get_cash())
            self.tick()
            strategy.tick()
        print(strategy.get_order_log())


# plot_stock([stock_list[0].get_main_stock(), stock_list[0].get_normal_stock(0), stock_list[0].get_normal_stock(1),
#             stock_list[0].get_normal_stock(2), stock_list[0].get_epsilon_data()])

LDE = LowDelayEnvironment()
LDE.run()
