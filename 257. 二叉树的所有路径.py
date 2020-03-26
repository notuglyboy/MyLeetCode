    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = [(root, '')]
        result = []
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                result.append('{}{}'.format(path, node.val))
            stack.append((node.right, '{}{}->'.format(path, node.val)))
            stack.append((node.left, '{}{}->'.format(path, node.val)))
        return result