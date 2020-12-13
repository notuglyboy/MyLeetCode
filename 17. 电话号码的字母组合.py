num_str = {
	"2": "abc",
	"3": "def",
	"4": "ghi",
	"5": "jkl",
	"6": "mno",
	"7": "pqrs",
	"8": "tuv",
	"9": "wxyz",
}

result = []
def letterCombinations(digits):
	inner_str = ""
	dfs(inner_str, digits)

def dfs(str_t, c):
	if not c:
		if str_t:
			result.append(str_t)
		return
	current_num = c[0]
	tags = num_str[current_num]
	for tag in tags:
		stack_str = str_t
		stack_str += tag
		dfs(stack_str, c[1:])