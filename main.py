from stocks import Stock, StockInfo
from bot import Bot, BotMathInfo
from order import Order, OrderInfo
from time import time
from numpy.random import normal
import matplotlib.pyplot as plt
from numpy.random import seed, randint
from numpy.random import choice
from numpy.random import lognormal
import numpy as np
from bot import generate_normal_distribution_from_price

STOCK_TIMELINE = 365


def generate_stock(seed_int):
    seed(seed_int)
    stock_data = [randint(4, 450)]
    if i == 29:
        print(stock_data)
    trend = randint(-200, 200) / 1000
    for _ in range(STOCK_TIMELINE):
        next_price = trend + abs(normal(stock_data[-1], 0.5, 1)[0])
        stock_data.append(next_price)
    return Stock(f"{seed_int}", StockInfo(f"seed {seed_int}", "randomly generated", stock_data))


stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))

test_stock = stock_list[30]

print(test_stock.get_current_price(), test_stock.get_next_checkpoint())
test_bots = []
for i in range(50):
    test_bot = Bot(test_stock, BotMathInfo((0.05, 0.05), (1000, 1000)))
    test_bot.generate_stock_bs_chart()
    test_bots.append(test_bot)

# Given current price, select a buy/sell order to process
for i, bot in enumerate(test_bots):
    bi = bot.generate_stock_bs_chart()
    number = round(choice(bi), 2)
    print(bi)
    print(number, test_stock.info.get_buy_shares(number))
    # print(round(choice(bi), 2), test_stock.info.buyOrders[round(choice(bot), 2)][0].get_shares())
# print(generate_normal_distribution_from_price(test_stock.get_current_price()))





# btc = Stock("BTC", StockInfo("Bitcoin", 3, "Crypto"))
# eth = Stock("BTC", StockInfo("Ethereum", 3.1, "Crypto"))
#
# btc_bot = Bot(btc, BotMathInfo((0.05, 0.05), (10000, 10000)))
# eth_bot = Bot(eth, BotMathInfo((0.05, 0.05), (10000, 10000)))
# btc_bot.generate_stock_bs_chart()
# eth_bot.generate_stock_bs_chart()
# print(btc.get_current_price())
# print(eth.get_current_price())
# eth.add_order(Order("1", "sell", OrderInfo(3, 3213, time(), False)))
# # eth.print_table()
# print(eth.info.calculate_share_price())