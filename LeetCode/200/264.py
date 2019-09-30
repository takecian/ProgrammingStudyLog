class Solution(object):
    def nthUglyNumber(self, n):
        i2 = 0
        i3 = 0
        i5 = 0
        dp = [1]
        while len(dp) < n:
            val = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            dp.append(val)
            if val == dp[i2] * 2:
                i2 += 1
            if val == dp[i3] * 3:
                i3 += 1
            if val == dp[i5] * 5:
                i5 += 1
        return dp[-1]