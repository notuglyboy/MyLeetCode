def generate(numRows: int):
	new_row = [1]
	for i in range(1, numRows+1):
		last_row = new_row
		new_row = [1]
		n = 0
		while n <= len(last_row) - 2:
			new_row.append(last_row[n] + last_row[n+1])
			n+=1
		new_row.append(1)
	return new_row