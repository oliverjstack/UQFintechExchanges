from numpy.random import normal, seed
import numpy as np
from order import Order, OrderInfo
from time import time
from stocks import Stock
import matplotlib.pyplot as plt
def generate_normal_distribution_from_price(mean):
    norm = sorted(normal(mean, 0.1, 1000))
    for index, num in enumerate(norm):
        norm[index] = round(norm[index], 2)
    return norm


def generate_prob_distribution(stock):
    norm = generate_normal_distribution_from_price(stock.get_current_price())

    probability = {}
    for num in norm:
        if num not in probability:
            probability[num] = 1
        else:
            probability[num] += 1
    for num, occurrence in probability.items():
        probability[num] = occurrence / 1000

    return probability


class BotMathInfo:
    sigma_buy: float
    sigma_sell: float
    mu_buy: float
    mu_sell: float
    buy_vol: int
    sell_vol: int

    def __init__(self, mus, vols):
        self.mu_buy = mus[0]
        self.mu_sell = mus[1]
        self.buy_vol = vols[0]
        self.sell_vol = vols[1]

    def set_sigmas(self, stock):
        self.sigma_buy = generate_normal_distribution_from_price(stock.get_current_price())[0]
        self.sigma_sell = generate_normal_distribution_from_price(stock.get_current_price())[-1]

    def get_buy_info(self):
        return self.sigma_buy, self.mu_buy

    def get_sell_info(self):
        return self.sigma_sell, self.mu_sell

    def get_buy_vol(self):
        return self.buy_vol

    def get_sell_vol(self):
        return self.sell_vol


class Bot:
    stock: Stock
    stats: BotMathInfo

    def __init__(self, stock, stats):
        self.stock = stock
        self.stats = stats
        self.stats.set_sigmas(self.stock)

    def generate_stock_bs_chart(self):
        mu, sigma = self.stats.get_buy_info()
        mu2, sigma2 = self.stats.get_sell_info()
        buy_dis = normal(mu, sigma, self.stats.get_buy_vol())
        sell_dis = normal(mu2, sigma2, self.stats.get_sell_vol())
        bimodal = np.concatenate([buy_dis, sell_dis])


        for index, num in enumerate(bimodal):
            bimodal[index] = round(bimodal[index], 2)

        volume = {}
        for num in bimodal:
            if num not in volume:
                volume[num] = 1
            else:
                volume[num] += 1

        for index, (price, vol) in enumerate(volume.items()):
            info = OrderInfo(price, vol, time(), False)
            if price < self.stock.get_current_price():
                self.stock.add_order(Order(f"{index}", "buy", info))
            else:
                self.stock.add_order(Order(f"{index}", "sell", info))
        return bimodal
