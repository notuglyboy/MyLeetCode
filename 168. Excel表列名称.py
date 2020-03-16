def convertToTitle(n):
	result = ''
	start =ord('A')
	
	while n:
		n -=1
		i = n % 26
		t = chr(i+start)
		n = int(n /26) 
		result = t+result
	return result
	
f = convertToTitle(701)
print(f)
