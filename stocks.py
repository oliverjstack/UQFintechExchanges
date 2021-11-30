from numpy.random import randint


class Stock:
    stockId: int
    main_stock_data: list
    normal_dist: list
    epsilon_random_data: list

    def __init__(self, stockId, main_stock_data, normal_dist, epsilon_random_data):
        self.stockId = stockId
        self.main_stock_data = main_stock_data
        self.normal_dist = normal_dist
        self.epsilon_random_data = epsilon_random_data
        exchanges = ["A", "B", "C", "D", "E"]
        self.exchange_following = {}
        while len(exchanges) > 0:
            exchange = exchanges.pop(randint(0, len(exchanges)))
            if len(exchanges) == 4:
                self.exchange_following[exchange] = self.main_stock_data
            elif len(exchanges) in (3, 2, 1):
                self.exchange_following[exchange] = self.normal_dist[3 - len(exchanges)]
            elif len(exchanges) == 0:
                self.exchange_following[exchange] = self.epsilon_random_data

    def get_exchange_stock(self, exchange):
        return self.exchange_following[exchange]

    def get_main_stock(self):
        return self.main_stock_data

    def get_normal_stock(self, number):
        return self.normal_dist[number]

    def get_epsilon_data(self):
        return self.epsilon_random_data

    def get_id(self):
        return self.stockId
