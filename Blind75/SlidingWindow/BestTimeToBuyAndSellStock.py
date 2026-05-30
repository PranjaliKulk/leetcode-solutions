def buy_and_sell_stock(prices):
    left = right = 0
    max_profit = 0

    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        
    return max_profit

prices = [10,1,5,6,7,1]
print(buy_and_sell_stock(prices))