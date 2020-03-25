def invertTree(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        #print(node.val)
        stack.append(node.right)
        stack.append(node.left)
        old_l = node.left 
        old_r = node.right
        node.left = old_r
        node.right = old_l