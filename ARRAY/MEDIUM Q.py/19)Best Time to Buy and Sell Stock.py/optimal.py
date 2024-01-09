# METHOD--(USING GREEDY APPROACH)

# In order to maximize the profit, we have to minimize the cost price and maximize the selling price. So at every step, we will keep track of the minimum buy price of stock encountered so far. If the current price of stock is lower than the previous buy price, then we will update the buy price, else if the current price of stock is greater than the previous buy price then we can sell at this price to get some profit. After iterating over the entire array, return the maximum profit.

# STEPS--

# 1) Declare a buy variable to store the min stock price encountered so far and max_profit to store the maximum profit.

# 2) Initialize the buy variable to the first element of the prices array.

# 3) Iterate over the prices array and check if the current price is less than buy price or not.

#    A) If the current price is smaller than buy price, then buy on this ith day.

#    B) If the current price is greater than buy price, then make profit from it and maximize the max_profit.

# 4) Finally, return the max_profit.

# CODE--
def maxProfit(prices, n):
    buy = prices[0]
    max_profit = 0
    for i in range(1,n):

        # Checking for lower buy value
        if (buy>prices[i]):
            buy = prices[i]

        # Checking for higher profit
        elif (prices[i] - buy >  max_profit):
            max_profit = prices[i] - buy
    return max_profit

# Driver code
if __name__ == '__main__':
    prices = [7,1,5,6,4]
    n= len(prices)
    max_profit = maxProfit(prices,n)
    print(max_profit)        


# Output--
# 5

# Time Complexity: O(N). Where N is the size of prices array. 

# Auxiliary Space: O(1)


