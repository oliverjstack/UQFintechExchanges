class StockInfo:
    name: str
    currentPrice: int
    stockType: str
    buyOrders: dict
    sellOrders: dict

    def __init__(self, name, currentPrice, stockType, orders=None):
        self.name = name
        self.currentPrice = currentPrice
        self.stockType = stockType
        if orders is None:
            self.orders = []
        else:
            self.orders = orders

    def update_price(self, price):
        self.currentPrice = price

    def append_buy(self, order):
        self.buyOrders[ord]

    def append_sell(self, order):
        self.sellOrders[order]

    def get_order_list(self):
        return self.orders

    def __str__(self):
        return f"{self.name} stock ({self.stockType}) at {self.currentPrice}"


class Stock:
    stockId: int
    info: StockInfo

    def __init__(self, stockId, info):
        self.stockId = stockId
        self.info = info

    def __str__(self):
        return f"<{self.stockId}> " + self.info.__str__()
