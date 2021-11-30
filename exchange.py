from bot import *
from order import Order


class Exchange:
    delay: int
    order_queue: list
    name: str
    bps: float

    def __init__(self, exchange_number, delay, bps):
        self.order_queue = []
        self.delay = delay
        self.name = exchange_number
        self.bps = bps
        self.day = 0

    def get_stock(self, stock):
        return stock.get_exchange_stock(self.name)

    def get_name(self):
        return self.name

    def queue_order(self, order):
        self.order_queue.append([order, self.delay])
        self.order_queue.sort(key=lambda x: x[1])

    def get_queued_orders(self):
        return self.order_queue

    def process_order(self, order: Order):
        cash = order.get_shares() * self.get_stock(order.get_stock())[self.day] + \
               (order.get_shares() * self.get_stock(order.get_stock())[self.day] * self.bps)
        if order.get_type() == "buy":
            if can_buy(order.get_trader(), cash):
                order.get_trader().update_cash(-1 * round(cash, 2))
                order.get_trader().add_shares(order.get_stock().get_id(), order.get_shares())
        else:
            order.get_trader().update_cash(cash)
            order.get_trader().remove_shares(order.get_stock(), order.get_shares())

    def tick(self):
        for order in self.order_queue:
            order[1] -= 1

        remove_list = []
        for i, order in enumerate(self.order_queue):
            if order[1] == 0:
                self.process_order(order[0])
                remove_list.append(i)

        for index in remove_list:
            self.order_queue.pop(index)

        self.day += 1


