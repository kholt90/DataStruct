
import random

# Options
seed = 100
size = 10
iterations = 5

random.seed(100)

def get_max_profit(prices):
    buy = 0
    sell = 1
    profit = 0
    for index, price in enumerate(prices):
        if (prices[index] < prices[buy]):
            buy = index
        elif (index > buy) and (prices[index] > prices[sell]):
            sell = index
        if sell > buy:
            profit = prices[sell] - prices[buy]
    return profit

for i in range(iterations):
    stock_prices = []
    # stock_prices = [15, 20, 10]
    # stock_prices = [20, 15, 10]
    for i in range(size):
        stock_prices.append(random.randint(1, 100))

    print(f"Stock Prices: {stock_prices}")

    profit = get_max_profit(stock_prices)
    print(f"Best profit for yesterday is ${profit}\n")
