from order import Order
import matplotlib.pyplot as plt


class StockInfo:
    name: str
    currentPrice: int
    stockType: str
    buyOrders: dict
    sellOrders: dict
    stock_data: list

    def __init__(self, name, currentPrice, stockType, stock_data):
        self.name = name
        self.currentPrice = currentPrice
        self.stockType = stockType
        self.stock_data = stock_data
        self.buyOrders = {}
        self.sellOrders = {}

    def update_price(self, price):
        self.currentPrice = price

    def append_order(self, order: Order):
        if order.get_type() == "buy":
            if order.get_price() not in self.buyOrders:
                self.buyOrders[order.get_price()] = [order]
            else:
                self.buyOrders[order.get_price()].append(order)
        else:
            if order.get_price() not in self.sellOrders:
                self.sellOrders[order.get_price()] = [order]
            else:
                self.sellOrders[order.get_price()].append(order)

    def get_sell(self):
        return self.sellOrders

    def get_buy(self):
        return self.buyOrders

    def get_buy_shares(self, price):
        orders = self.buyOrders[price]
        ret = 0
        for order in orders:
            ret += order.get_shares()
        return ret

    def get_sell_shares(self, price):
        orders = self.sellOrders[price]
        ret = 0
        for order in orders:
            ret += order.get_shares()
        return ret

    def print_table(self):
        prices = sorted(list(list(self.buyOrders) + list(self.sellOrders)), reverse=True)
        checked = []
        print("{: >10} | {: >10} || {: >10} | {: >10}".format("Price", "Buy", "Price", "Sell"))
        print("{: >40}".format("-"*50))
        for price in prices:
            if price not in checked:
                if price in self.sellOrders and price in self.buyOrders:
                    print("{: >10} | {: >10} || {: >10} | {: >10}".format(price, self.get_buy_shares(price), price,
                                                                          self.get_sell_shares(price)))
                elif price in self.buyOrders:
                    print("{: >10} | {: >10} || {: >10} | {: >10}".format(price, self.get_buy_shares(price), "-", "-"))
                elif price in self.sellOrders:
                    print("{: >10} | {: >10} || {: >10} | {: >10}".format("-", "-", price, self.get_sell_shares(price)))
                else:
                    print("{: >10} | {: >10} || {: >10} | {: >10}".format("-", "-", "-", "-"))
            checked.append(price)

    def get_current_price(self, day):
        return self.stock_data[day - 1]

    def calculate_share_price(self):
        summation = 0
        share_count = 0
        for price in self.buyOrders.keys():
            shares = self.get_buy_shares(price)
            summation += price*shares
            share_count += shares

        for price in self.sellOrders.keys():
            shares = self.get_sell_shares(price)
            summation += price * shares
            share_count += shares
        return summation / share_count

    def __str__(self):
        return f"{self.name} stock ({self.stockType}) at {self.currentPrice}"


class Stock:
    stockId: int
    day: int
    info: StockInfo

    def __init__(self, stockId, info, day=1):
        self.stockId = stockId
        self.info = info
        self.day = day

    def print_table(self):
        self.info.print_table()

    def get_current_price(self):
        return self.info.get_current_price(self.day)

    def add_order(self, order):
        self.info.append_order(order)

    def plot_stock(self, days):
        plt.plot(list(range(days)), self.info.stock_data)
        plt.show()

    def __str__(self):
        return f"<{self.stockId}> " + self.info.__str__()

    def __repr__(self):
        return f"<{self.stockId}> " + self.info.__str__()
