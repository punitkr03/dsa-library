def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    lptr = 0
    rptr = 1
    max_profit = 0
    while (rptr < len(prices)):
        if(prices[rptr] > prices[lptr]):
            profit = prices[rptr] - prices[lptr]
            max_profit = max(max_profit, profit)
        else:
            lptr = rptr
        rptr +=1
    return max_profit
        
print(maxProfit(prices=[7,1,5,3,6,4]))
