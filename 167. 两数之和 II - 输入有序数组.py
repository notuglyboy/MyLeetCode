def twoSum(numbers, target):
	if not numbers:
		return []
	big = len(numbers) -1 
	small = 0
	while big > small:
		sum1 = numbers[big] + numbers[small]
		print(numbers[big], numbers[small])
		if sum1 == target:
			return [small+1, big+1]
		elif sum1 > target:
			big -= 1
		else:
			small += 1
	return []




f = twoSumErfen([3,24,50,79,88,150,345], 200)
print(f)