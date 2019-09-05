class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        imax = ans
        imin = ans

        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            ans = max(ans, imax)

        return ans