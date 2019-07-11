import bisect
from collections import defaultdict


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                k = i
        if k == -1:  # most big
            nums.reverse()
            return

        j = k + 1
        i = k + 1
        while i < len(nums):
            if nums[k] < nums[i]:
                j = i
            i += 1

        nums[j], nums[k] = nums[k], nums[j]

        l = k + 1
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return
