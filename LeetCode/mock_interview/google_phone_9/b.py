class Solution(object):
    def getMoneyAmount(self, n):
        dp = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                dp[lo][hi] = min([x + max(dp[lo][x-1], dp[x+1][hi]) for x in range(lo, hi)])
        return dp[1][n]
