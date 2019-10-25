class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        if len(nums) == 0:
            return 0

        if len(nums) < 3:
            return max(nums)

        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 3], dp[i - 2])

        return max(dp[-2], dp[-1])
