
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def fontprint(node):
    if node.left == None and node.right == None:
        print(node.val)
        return
    print(node.val)
    fontprint(node.left)
    fontprint(node.right)

def fontprintr(node):
    if node.left == None and node.right == None:
        print(node.val)
        return
    print(node.val)
    fontprintr(node.right)
    fontprintr(node.left)

def isSymmetric(root: TreeNode) -> bool:
    l = [root, root]
    while l:
        node1 = l.pop()
        node2 = l.pop()

        if node1 == None and node2 == None:
            continue
        print(node1.val, node2.val)
        if node1.val != node2.val:
            return False
        l.append(node1.left)
        l.append(node2.right)
        l.append(node2.left)
        l.append(node1.right)
    return True

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

if __name__ == "__main__":
    r = insertTree([1,2,2,None,3,None,3])
    d = isSymmetric(r)
    print(d)
    #fontsearch
    #fontprint(r)
    