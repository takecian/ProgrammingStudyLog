# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums):
        ans = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            ans = max(ans, current_sum)
            current_sum = max(0, current_sum)

        return ans
