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

def listTree(node, dep):
    if not node or (not node.left and not node.right):
        return dep
    left = right = dep
    
    left =  listTree(node.left, dep)
    right =  listTree(node.right, dep)

    if  not node.left:
        left = right
    if not node.right:
        right = left
    return min(left, right) + 1

import queue
node_queue = queue.Queue()
def listTreeQueue(root, sum):
    if not root:
        return False
    node_queue = [(root, sum)]
    last_node_end = root
    while node_queue:
        node,remain = node_queue[0]
        del node_queue[0]
        print(node.val)
        remain -= node.val
        if not node.left and not node.right and remain == 0:
            return True
        if node.left:
            node_queue.append((node.left, remain))
        if node.right:
            node_queue.append((node.right, remain))

        if last_node_end == node:
            if node_queue:
                last_node_end = node_queue[-1]
    return False

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    d = listTreeQueue(root)
    return  d



if __name__ == "__main__":
    s = buildTree([-2, None, -3])
    g = listTreeQueue(s, -5)
    print(g)

