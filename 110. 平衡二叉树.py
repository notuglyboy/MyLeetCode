def listtree(node, depth):
    if not node or (not node.left and not node.right):
        return depth

    left = listtree(node.left, depth if node.left else 0)
    if left == -1:
        return -1
    right = listtree(node.right, depth if node.right else 0)
    if right == -1:
        return -1
    return max(left , right) + 1 if abs(left - right) <= 1 else -1


def isBalanced(self, root: TreeNode) -> bool:
    return listtree(root, 1) != -1