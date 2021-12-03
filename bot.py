from numpy.random import normal, seed, randint
from stocks import Stock
import matplotlib.pyplot as plt

STOCK_TIMELINE = 1095
EXCHANGES = ["A", "B", "C", "D", "E"]


def generate_stock(seed_int):
    seed(seed_int)
    k_main = 0.2
    epsilon_main = 0
    k_abnormal = 0.023
    epsilon_abnormal = 0.3
    main_stock_data = [randint(4, 450)]
    normal_dist_data = [[], [], []]
    abnormal_data = [main_stock_data[-1] + normal(epsilon_abnormal, k_abnormal, 1)[0]]
    for i in range(3):
        normal_dist_data[i].append(main_stock_data[-1] + normal(epsilon_main, k_main, 1)[0])
    trend = randint(-50, 50) / 1000
    for _ in range(STOCK_TIMELINE):
        next_price = trend + normal(main_stock_data[-1], 0.5, 1)[0]
        if next_price < 0:
            next_price = trend + abs(normal(main_stock_data[-1], 0.5, 1)[0])
        for i in range(3):
            normal_dist_data[i].append(next_price + normal(epsilon_main, k_main, 1)[0])
        abnormal_data.append(next_price + normal(epsilon_abnormal, k_abnormal, 1)[0])
        main_stock_data.append(next_price)
    return Stock(seed_int, main_stock_data, normal_dist_data, abnormal_data)


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
