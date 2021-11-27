from stocks import Stock, StockInfo
from bot import Bot, BotMathInfo
from order import Order, OrderInfo
from time import time

btc = Stock("BTC", StockInfo("Bitcoin", 3, "Crypto"))
eth = Stock("BTC", StockInfo("Ethereum", 3.1, "Crypto"))

btc_bot = Bot(btc, BotMathInfo((0.05, 0.05), (10000, 10000)))
eth_bot = Bot(eth, BotMathInfo((0.05, 0.05), (10000, 10000)))
btc_bot.generate_stock_bs_chart()
eth_bot.generate_stock_bs_chart()
print(btc.get_current_price())
print(eth.get_current_price())
eth.add_order(Order("1", "sell", OrderInfo(3, 3213, time(), False)))
# eth.print_table()
print(eth.info.calculate_share_price())
