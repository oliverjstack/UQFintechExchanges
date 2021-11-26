from order import Order, OrderInfo
from stocks import Stock, StockInfo
from time import time
from numpy.random import normal
import numpy as np
import matplotlib.pyplot as plt

norm = sorted(normal(1.0, 0.05, 1000))
for index, num in enumerate(norm):
    norm[index] = round(norm[index], 2)

sales = {}
for num in norm:
    if num not in sales:
        sales[num] = 1
    else:
        sales[num] += 1

sum = 0
for price, shares in sales.items():
    sum += price * shares
print(round(sum / 1000, 2))
print(sales)

mu, sigma = norm[0], 0.05
mu2, sigma2 = norm[-1], 0.05
buy_dis = normal(mu, sigma, 1000)
sell_dis = normal(mu2, sigma2, 1000)
X = np.concatenate([buy_dis, sell_dis])
print(X)
plt.hist(X)
plt.show()



btc = Stock("BTC", StockInfo("Bitcoin", 1, "Crypto"))
orders = [Order("1", "buy", OrderInfo(1.01, 5000, time(), False)),
          Order("5", "sell", OrderInfo(1.01, 50, time(), False)),
          Order("5", "sell", OrderInfo(1.01, 50, time(), False)),
          Order("2", "buy", OrderInfo(0.98, 5000, time(), False)),
          Order("3", "sell", OrderInfo(1.03, 5000, time(), False)),
          Order("4", "sell", OrderInfo(0.97, 5000, time(), False))]

for order in orders:
    btc.info.append_order(order)

btc.print_table()
print(btc.info.calculate_share_price())
