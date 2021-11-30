class Trader:
    stocks_owned: dict
    cash: float
    previous_orders: list

    def __init__(self, cash):
        self.stocks_owned = {}
        for i in range(100):
            self.stocks_owned[i] = 0
        self.cash = cash
        self.previous_orders = []

    def get_cash(self):
        return self.cash

    def update_cash(self, price):
        self.cash += price

    def get_shares_owned(self, stock):
        return self.stocks_owned[stock]

    def add_shares(self, stock, shares):
        self.stocks_owned[stock] += shares

    def remove_shares(self, stock, shares):
        self.stocks_owned[stock] += shares
