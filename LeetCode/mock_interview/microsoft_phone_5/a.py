class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        m = len(nums) // 2
        node = TreeNode(nums[m])
        node.left = self.sortedArrayToBST(nums[:m])
        node.right = self.sortedArrayToBST(nums[m + 1:])

        return node