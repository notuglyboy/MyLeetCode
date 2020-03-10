class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def insertTree(nums):
    stack = []
    i = 0
    root = None
    while i < len(nums):
        if not stack:
            a = TreeNode(nums[i])
            stack.append(a)
            i+=1
            root = a
        else:
            a = stack.pop()
            right = TreeNode(nums[i+1])
            left = TreeNode(nums[i])
            a.left = left
            a.right = right
            top = None
            if stack:
                top = stack.pop()
            stack.append(right)
            stack.append(left)
            if top:
                stack.append(top)
            i+=2
    return root

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

def judge(node1, deep):
    if node1 == None:
        return deep
    left =judge(node1.left, deep)
    right = judge(node1.right, deep)
    return max(left, right) + 1

def maxDepth(root: TreeNode) -> int:
    d = judge(root, 0)
    return d

if __name__ == "__main__":
    r = buildTree([3,9,20,None,None,15,7])
    d = maxDepth(r.left)
    print(d)
    #print(r.left.right)