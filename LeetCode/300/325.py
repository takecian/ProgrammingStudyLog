class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_index = {}
        cumulsum = 0
        sum_index[0] = 0
        for i in range(len(nums)):
            cumulsum += nums[i]
            if cumulsum - k in sum_index:
                ans = max(ans, i - sum_index[cumulsum - k] + 1)

            if cumulsum not in sum_index:
                sum_index[cumulsum] = i + 1

        return ans
