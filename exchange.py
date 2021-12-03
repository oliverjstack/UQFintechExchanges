from bot import *
from order import Order
from typing import List, Dict, Tuple


class CentralHub:
    delay: Dict[str, int]
    order_queue: Dict[str, List[list]]
    bps: dict
    day: int

    def __init__(self, delay, bps):
        self.delay = delay
        self.bps = bps
        self.order_queue = dict()
        for exchange in EXCHANGES:
            self.order_queue[exchange] = []
        self.day = 0

    def get_day(self):
        return self.day

    def queue_order(self, order: Order, exchange: str):
        self.order_queue[exchange].append([order, self.delay[exchange]])

    def process_order(self, order: Order, exchange: 'Exchange'):
        cash = order.get_shares() * exchange.get_stock_price(order.get_stock()) + \
               (order.get_shares() * exchange.get_stock_price(order.get_stock()) * self.bps[exchange.get_name()])
        if order.get_type() == "buy":
            if can_buy(order.get_trader(), cash):
                order.get_trader().update_cash(-1 * round(cash, 2))
                order.get_trader().add_shares(order.get_stock(), order.get_shares())
        else:
            order.get_trader().update_cash(cash)
            order.get_trader().remove_shares(order.get_stock(), order.get_shares())

    def tick(self, exchanges):
        for exchange in exchanges:
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

        self.day += 1


class Exchange:
    name: str
    stock_list: List[list]
    _central_hub: CentralHub

    def __init__(self, exchange_number, stock_list, central_hub):
        self.name = exchange_number
        self.stock_list = [[] for _ in range(100)]
        for stock in stock_list:
            self.stock_list[stock.get_id()] = stock.get_exchange_stock(self.name)
        self._central_hub = central_hub

    def get_stock_price(self, stock):
        return self.get_stock_data(stock)[-1]

    def get_stock_data(self, stock):
        return self.stock_list[stock][:self._central_hub.get_day() + 1]

    def get_name(self):
        return self.name

    def queue_order(self, order):
        self._central_hub.queue_order(order, self.name)


