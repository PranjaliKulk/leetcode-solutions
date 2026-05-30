# Keep track of cheapest price so far
# at every lowest price, calculate the profit -> return max profit value
# Time: O(n) Space: O(1)

def maxProfit(prices):
    min_price = float('inf') # start with infinity to rightfuly store min value
    profit = 0 # No profit yet

    for price in prices:
        # update min price so far
        if price < min_price:
            min_price = price
        # calculate profit
        else:
            profit = price - min_price # calcuate profit for current two elements
            max_profit = max(profit, max_profit) # store max of current profit and old max profit

    return max_profit