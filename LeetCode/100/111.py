class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = [(root, 1)]
        while que:
            node, depth = que.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))