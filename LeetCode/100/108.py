# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        m = (0 + len(nums) - 1) // 2
        node = TreeNode(nums[m])
        left = nums[:m]
        node.left = self.sortedArrayToBST(left)

        right = nums[m + 1:]
        node.right = self.sortedArrayToBST(right)

        return node