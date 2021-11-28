from stocks import Stock, StockInfo
from bot import Bot, BotMathInfo
from order import Order, OrderInfo
from time import time
from numpy.random import normal
import matplotlib.pyplot as plt
from random import randint
from numpy.random import seed

STOCK_TIMELINE = 365


def generate_stock(seed_int):
    seed(seed_int)
    stock_data = [10]
    trend = randint(-200, 200) / 1000
    for _ in range(STOCK_TIMELINE):
        next_price = trend + abs(normal(stock_data[-1], 0.5, 1)[0])
        stock_data.append(next_price)
    return Stock(f"{seed_int}", StockInfo(f"seed {seed_int}", randint(0, 450), "randomly generated", stock_data))


stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))
print(stock_list)

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