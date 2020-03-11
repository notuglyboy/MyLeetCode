def maxProfit(prices) -> int:
	temp = 0
	for i in prices:
		temp ^= i
	return temp
