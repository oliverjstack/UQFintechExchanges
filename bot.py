from numpy.random import normal, seed, randint
from stocks import Stock, StockInfo
import numpy as np
STOCK_TIMELINE = 365

def generate_volume_distribution(normal_distribution):
    return generate_bimodal_distribution((normal_distribution[0], normal_distribution[-1]), (0.1, 0.1), (1000, 1000))


def generate_buy_distribution(normal_distribution):
    return generate_bimodal_distribution((normal_distribution[0], normal_distribution[-1]), (0.05, 0.05), (1900, 100))


def generate_sell_distribution(normal_distribution):
    return generate_bimodal_distribution((normal_distribution[0], normal_distribution[-1]), (0.05, 0.05), (100, 1900))


def generate_normal_distribution_from_price(stock):
    norm = sorted(normal(stock.get_current_price(), 0.1, 1000))
    for index, num in enumerate(norm):
        norm[index] = round(norm[index], 2)
    return norm


def generate_bimodal_distribution(mu, sigma, volume):
    buy_dis = normal(mu[0], sigma[0], volume[0])
    sell_dis = normal(mu[1], sigma[1], volume[1])
    bimodal = np.concatenate([buy_dis, sell_dis])
    return bimodal


def generate_stock(seed_int):
    seed(seed_int)
    stock_data = [randint(4, 450)]
    trend = randint(-200, 200) / 1000
    for _ in range(STOCK_TIMELINE):
        next_price = trend + normal(stock_data[-1], 0.5, 1)[0]
        if next_price == 0:
            next_price = trend + abs(normal(stock_data[-1], 0.5, 1)[0])
        stock_data.append(next_price)
    return Stock(f"{seed_int}", StockInfo(f"seed {seed_int}", "randomly generated", stock_data))


def get_shares(price, processed_orders):
    orders = processed_orders[price]
    ret = 0
    for order in orders:
        ret += order.get_shares()
    return ret

