from order import Order, OrderInfo
from stock import Stock, StockInfo
from time import time


stock = Stock("1", StockInfo("Tesla", 1116.00, "Energy"))
newOrder = Order("231", "buy", OrderInfo(10, time(), False))
print(stock)
print(newOrder)
stock.info.append_order(newOrder)
print(stock.info.buyOrders)