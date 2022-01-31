from typing import List


class Exchange:
    """
    Exchange object representing a simulated exchange
    """
    name: str
    stock_list: List[list]
    day: int

    def __init__(self, exchange_name, stock_list):
        """
        Creates an exchange object
        :param exchange_name: Name of the exchange
        :param stock_list: Stocks for this exchange
        """
        self.name = exchange_name
        self.day = 0
        self.stock_list = [[] for _ in range(100)]
        for stock in stock_list:
            self.stock_list[stock.get_id()] = stock.get_exchange_stock(self.name)

    def get_stock_price(self, stock):
        """
        Returning the most up to date price of a given stock
        :param stock: Stock number to retrieve
        :return: Most up to date price
        """
        return self.get_stock_data(stock)[-1]

    def get_stock_data(self, stock):
        """
        Return all data for a given stock up until and including the most recent price
        :param stock: Stock number to retrieve
        :return: A list of prices for the stock
        """
        return self.stock_list[stock][:self.day + 1]

    def get_name(self):
        """
        Return the name of the exchange
        :return: Name of the exchange
        """
        return self.name

    def tick(self):
        """
        Updates the internal exchanges time period
        """
        self.day += 1


