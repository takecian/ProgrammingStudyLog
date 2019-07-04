# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.left is None and root.right is None and p.val < root.val:
            return root

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            node = self.inorderSuccessor(root.left, p)
            if node is None:
                return root
            else:
                if node.val < root.val:
                    return node
                else:
                    return root

