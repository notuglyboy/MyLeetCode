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

def afterprintStack(root):
    stack = [root]
    last_node = root
    while stack:
        node = stack.pop()
        if not node:
            last_node = None
            continue
        if node.left and last_node != node.left and node.right != last_node:
            stack.append(node)
            stack.append(node.left)
            continue
        elif node.right and node.right != last_node:
            stack.append(node)
            stack.append(node.right)
            continue
        if node.right == last_node or not node.right or (not node.right and not node.left):
            print(node.val)
            last_node = node
            continue

def judge(self, node1, node2):
    if node1 == None and node2 == None:
        return True
    if node1 == None or node2 == None:
        return False
    if node1.val != node2.val:
        return False
    left = self.judge(node1.left, node2.left)
    right = self.judge(node1.right, node2.right)
    return left and right

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

def midprintStack(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            stack.append(node.left)
        else:
            if stack:
                tmp = stack.pop()
                print(tmp.val)
                stack.append(tmp.right)

 
 
def frontprintStack(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        print(node.val)
        stack.append(node.right)
        stack.append(node.left)
    
def listtree(node, depth):
    if not node or (not node.left and not node.right):
        return depth

    left = listtree(node.left, depth if node.left else 0)
    if left == -1:
        return -1
    right = listtree(node.right, depth if node.right else 0)
    if right == -1:
        return -1
    print(left, right)
    return max(left , right) + 1 if abs(left - right) <= 1 else -1

def isBalanced(root: TreeNode) -> bool:
    d = listtree(root,1)
    return d

if __name__ == "__main__":
    s = buildTree([1,2,2,3,None,None,3,4,None,None,4])
    g = isBalanced(s)
    print(g)

