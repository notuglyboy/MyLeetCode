class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def buildTree(nums):
	stack = []
	i = 0
	while i < len(nums):
		d = 3



def buildTree(nums):
    root = TreeNode(nums[0])
    stack = [root]
    i = 1
    while i <= len(nums) - 1:
        node = stack.pop()
        if nums[i]:
            node.left = TreeNode(nums[i])
        if nums[i+1]:
            node.right = TreeNode(nums[i+1])
        top = None
        if stack:
            top = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if top:
            stack.append(top)
        i += 2

    return root

if __name__ == "__main__":
    s = buildTree([1,2,2,None,3,None,3])
    print(s.left.left)