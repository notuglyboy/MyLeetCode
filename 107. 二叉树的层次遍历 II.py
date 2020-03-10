def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
	stack = []
	
	result = []
	while stack:
		stack_n = []
		inner_list = []
		for i in stack:
			inner_list.append(i)
			if i.left:
				stack_n.append(i.left)
			if i.right:
				stack_n.append(i.right)
		stack = stack_n
		result.append(inner_list)
	return result
