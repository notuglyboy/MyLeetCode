def trailingZeroes(n):
	count = 0
	while n > 0:
		count += int(n /5);
		n = int(n/5)
	return count
f = trailingZeroes(30)
print(f)