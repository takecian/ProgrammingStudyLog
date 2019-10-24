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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def calc_depth(node, depth):
            if node.left is None and node.right is None:
                return depth

            ret = 10 ** 10
            if node.left:
                ret = min(ret, calc_depth(node.left, depth + 1))

            if node.right:
                ret = min(ret, calc_depth(node.right, depth + 1))
            return ret

        return calc_depth(root, 1)
