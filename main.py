from bot import *
from numpy.random import seed, randint, choice
from bot import generate_normal_distribution_from_price
from time import time
import matplotlib.pyplot as plt

stock_list = []
for i in range(100):
    stock_list.append(generate_stock(i))

normal_dist = generate_normal_distribution_from_price(stock_list[43])
plot_for_check_y = []
plot_for_check_x = []
while stock_list[43].get_checkpoint_number() < STOCK_TIMELINE:
    current_price, next_price = stock_list[43].get_current_price(), stock_list[43].get_next_checkpoint()
    loop = 1
    while True:
        sell = True
        if current_price < next_price:
            bimodal = generate_sell_distribution(normal_dist)
        else:
            sell = False
            bimodal = generate_buy_distribution(normal_dist)
        start = time()
        for i in range(50):
            seed(i * loop)
            order = round(choice(bimodal), 2)
            if order > stock_list[43].get_current_price():
                print(f"\033[31m sell {order}")
            else:
                print(f"\033[1;32m buy {order}")
            plot_for_check_y.append(order)
            plot_for_check_x.append(stock_list[43].get_checkpoint_number())
            stock_list[43].update_current_price(order)
        if (sell and stock_list[43].get_current_price() < stock_list[43].get_next_checkpoint()) or \
                (not sell and stock_list[43].get_current_price() > stock_list[43].get_next_checkpoint()):
            normal_dist = generate_normal_distribution_from_price(stock_list[43])
            loop += 1
        else:
            stock_list[43].update_checkpoint()
            break
plt.scatter(plot_for_check_x, plot_for_check_y)
plt.show()
print(stock_list[43].get_current_price())
print(stock_list[43].get_next_checkpoint())