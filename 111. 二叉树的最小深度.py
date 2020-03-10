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
def listTreeQueue(node1):
    node_queue = [node1]
    dep = 1
    last_node_end = node1
    while node_queue:
        node = node_queue[0]
        del node_queue[0]
        if not node.left and not node.right:
            return dep
        if node.left:
            node_queue.append(node.left)
        if node.right:
            node_queue.append(node.right)

        if last_node_end == node:
            dep += 1
            if node_queue:
                last_node_end = node_queue[-1]

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    d = listTreeQueue(root)
    return  d