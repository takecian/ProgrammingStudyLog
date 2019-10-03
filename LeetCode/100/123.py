class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]

        for k in range(1, 3):
            low = prices[0]
            for i in range(1, n):
                low = min(low, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - low)
            # print(dp)
        return dp[2][-1]
