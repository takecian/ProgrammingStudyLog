# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            ret1 = is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
            ret2 = is_mirror(node1.left, node2.left) and is_mirror(node1.right, node2.right)
            return ret1 or ret2

        return is_mirror(root1, root2)