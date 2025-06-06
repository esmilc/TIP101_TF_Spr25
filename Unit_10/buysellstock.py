'''
Problem 2: Best Time to Buy & Sell Stock
You are given a list of integers prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profit(prices):
	pass

Example #1:
Input: prices = [7,1,5,3,6,4]
Expected Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example #2:
Input: prices = [7,6,4,3,1]
Expected Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


'''

def max_profit(prices):
    if not prices:
        return 0
    min_price, max_profit = prices[0], 0
	
    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(profit, max_profit)

    return max_profit

prices = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(max_profit(prices))
print(max_profit(prices2))