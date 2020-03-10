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
    node_queue.put(node1)
    dep = 1
    last_node_end = node1
    while not node_queue.empty():
        node = node_queue.get_nowait()
        if not node.left and not node.right:
            return dep
        if node.left:
            node_queue.put(node.left)
        if node.right:
            node_queue.put(node.right)

        if last_node_end == node:
            dep += 1
            last_node_end = node.left or node.right
            
def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    d = listTree(root, 1)
    return  d