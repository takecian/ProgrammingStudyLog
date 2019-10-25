class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0

        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = k

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] * (k - 1) + dp[i - 1][1] * (k - 1)
            dp[i][1] = dp[i - 1][0]

        return sum(dp[-1])
