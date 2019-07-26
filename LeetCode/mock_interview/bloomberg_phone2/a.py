class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        use = max(nums[0] * nums[1], nums[-3] * nums[-2])
        return use * nums[-1]