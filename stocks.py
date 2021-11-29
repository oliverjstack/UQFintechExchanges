from order import Order, OrderInfo
import matplotlib.pyplot as plt
from time import time
from bot import *


class StockInfo:
    name: str
    current_price: int
    stock_type: str
    processed_order_list: list
    current_price_distribution: list
    checkpoint: int

    def __init__(self, name, stock_type, stock_data):
        self.name = name
        self.current_price = stock_data[0]
        self.stock_type = stock_type
        self.stock_data = stock_data
        self.checkpoint_price = stock_data[1]
        self.checkpoint = 1
        self.processed_order_list = []

    def update_price(self, price):
        self.current_price = price

    def get_current_price(self):
        return self.current_price

    def get_next_checkpoint(self):
        return self.stock_data[self.checkpoint]

    def __str__(self):
        return f"{self.name} stock ({self.stock_type}) at {self.current_price}"


class Stock:
    stockId: int
    info: StockInfo

    def __init__(self, stockId, info):
        self.stockId = stockId
        self.info = info

    def get_current_price(self):
        return self.info.get_current_price()

    def update_current_price(self, price):
        self.info.update_price(price)

    def get_next_checkpoint(self):
        return self.info.get_next_checkpoint()

    def plot_stock(self):
        plt.plot(list(range(len(self.info.stock_data))), self.info.stock_data)
        plt.show()

    def update_checkpoint(self):
        self.info.checkpoint += 1

    def get_checkpoint_number(self):
        return self.info.checkpoint

    def create_spread(self, bimodal, print_table=True):
        for index, num in enumerate(bimodal):
            bimodal[index] = round(bimodal[index], 2)

        volume = {}
        for num in bimodal:
            if num not in volume:
                volume[num] = 1
            else:
                volume[num] += 1

        ret = {}
        for index, (price, vol) in enumerate(volume.items()):
            info = OrderInfo(price, vol, time(), False)
            if price < self.get_current_price():
                ret[price] = [Order(f"{index}", "buy", info)]
            else:
                ret[price] = [Order(f"{index}", "sell", info)]
        if print_table:
            prices = sorted(list(list(ret)), reverse=True)
            checked = []
            print("{: >10} | {: >10} || {: >10} | {: >10}".format("Price", "Buy", "Price", "Sell"))
            print("{: >40}".format("-" * 50))
            for price in prices:
                if price not in checked:
                    if price < self.get_current_price():
                        print("{: >10} | {: >10} || {: >10} | {: >10}".format(price, get_shares(price, ret), "-",
                                                                              "-"))
                    elif price > self.get_current_price():
                        print("{: >10} | {: >10} || {: >10} | {: >10}".format("-", "-", price,
                                                                              get_shares(price, ret)))
                    else:
                        print("{: >10} | {: >10} || {: >10} | {: >10}".format("-", "-", "-", "-"))
                checked.append(price)

    def __str__(self):
        return f"<{self.stockId}> " + self.info.__str__()

    def __repr__(self):
        return f"<{self.stockId}> " + self.info.__str__()
