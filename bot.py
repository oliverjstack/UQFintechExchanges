from numpy.random import normal, seed, randint
from stocks import Stock
import numpy as np
import matplotlib.pyplot as plt

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
    k = 0.1
    epsilon = 0.8
    main_stock_data = [randint(4, 450)]
    normal_dist_data = [[], [], []]
    epsilon_data = [main_stock_data[-1] + normal(epsilon, k, 1)[0]]
    for i in range(3):
        normal_dist_data[i].append(main_stock_data[-1] + normal(0, k, 1)[0])
    trend = randint(-50, 50) / 1000
    for _ in range(STOCK_TIMELINE):
        next_price = trend + normal(main_stock_data[-1], 0.5, 1)[0]
        if next_price < 0:
            next_price = trend + abs(normal(main_stock_data[-1], 0.5, 1)[0])
        for i in range(3):
            normal_dist_data[i].append(next_price + normal(0, k + 0.3, 1)[0])
        epsilon_data.append(next_price + normal(epsilon, k, 1)[0])
        main_stock_data.append(next_price)
    return Stock(seed_int, main_stock_data, normal_dist_data, epsilon_data)


def get_shares(price, processed_orders):
    orders = processed_orders[price]
    ret = 0
    for order in orders:
        ret += order.get_shares()
    return ret


def plot_stock(stock_data):
    for i, stock in enumerate(stock_data):
        plt.plot(list(range(len(stock))), stock, label=f"{i}")
        plt.legend()
    plt.show()


def can_buy(trader, required_cash):
    return trader.get_cash() >= required_cash
