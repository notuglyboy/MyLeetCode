def titleToNumber(s):
	start =ord('A')
	result = 0
	j = 0
	for i in s[::-1]:
		result += (ord(i) - start+1) * 26**j
		j+=1
	return result
	print(result)

titleToNumber('AZ')