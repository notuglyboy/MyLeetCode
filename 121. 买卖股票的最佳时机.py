def maxProfit(prices) -> int:
	max = 0
	ready_min = prices[0]
	for price in prices:
		if ready_min > price:
			ready_min = price

		else:
			max = max if max > (price - ready_min) else (price - ready_min)
	return max

a = maxProfit([7,1,5,3,6,-1,5])
print(a)