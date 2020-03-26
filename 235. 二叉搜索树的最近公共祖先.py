    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                return node