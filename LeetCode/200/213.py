class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) < 4:
            return max(nums)

        def max_profit(l):
            dp = [0] * len(l)
            dp[0] = l[0]
            dp[1] = l[1]
            dp[2] = l[0] + l[2]

            for i in range(3, len(l)):
                dp[i] = l[i] + max(dp[i - 3], dp[i - 2])

            return max(dp[-2], dp[-1])

        nums1 = nums[1:]
        nums2 = nums[:-1]

        return max(max_profit(nums1), max_profit(nums2))
