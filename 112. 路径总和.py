def listTreeQueue(node1):
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