# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            left = node.left
            if left:
                if min_val < left.val < node.val:
                    # print('pass1', node.val)
                    pass
                else:
                    # print(min_val, left.val, node.val)
                    return False

            right = node.right
            if right:
                if node.val < right.val < max_val:
                    # print('pass2', node.val)
                    pass
                else:
                    # print(node.val, right.val, max_val)
                    return False

            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, -10 ** 10, 10 ** 10)