def maxProfit(prices) -> int:
    max = 0
    for i in range(1, len(prices)):
        tep = prices[i] - prices[i -1]
        if tep > 0:
            max += tep
    return max


a = maxProfit([7,1,5,3,6,0,5])
print(a)