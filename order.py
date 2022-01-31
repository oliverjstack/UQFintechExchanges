from player import Trader


class Order:
    """
    Order object designed to aid in formatting and organizing orders
    """
    stock: int
    trader: Trader
    shares: int
    order_type: str

    def __init__(self, stock, trader, shares, order_type):
        """
        Initializes order object.
        :param stock: Stock to be actioned on
        :param trader: The trader making the order
        :param shares: Shares to be actioned
        :param order_type: Option to buy or sell
        """
        self.stock = stock
        self.trader = trader
        self.shares = shares
        self.order_type = order_type

    def get_stock(self):
        """
        Returns a stock number
        :return: Int referring to stock
        """
        return self.stock

    def get_trader(self):
        """
        Return the trading who is actioning this order
        :return: Trader object representing trader actioning this order
        """
        return self.trader

    def get_shares(self):
        """
        Return amount shares being actioned
        :return: Int referring to shares being actioned
        """
        return self.shares

    def get_type(self):
        """
        Returns the type of the order
        :return: String representing buy or sell
        """
        return self.order_type

    def __repr__(self):
        """
        Order in string form
        :return: String representation of the order
        """
        return f"Order: {self.get_type()}:{self.get_shares()}:stock({self.get_stock()})"

    def __eq__(self, other):
        """
        Checks if orders are equal
        :param other: Other order
        :return: Returns if the orders are equal
        """
        return self.trader == other.trader and \
               self.order_type == other.order_type and \
               self.stock == other.stock and \
               self.shares == other.shares
