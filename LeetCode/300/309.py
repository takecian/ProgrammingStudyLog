class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        dp1 = [0] * len(prices)
        dp2 = [0] * len(prices)
        dp3 = [0] * len(prices)
        dp1[0] = 0
        dp2[0] = -prices[0]
        dp3[0] = -10 ** 10
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i - 1], dp3[i - 1])
            dp2[i] = max(dp2[i - 1], dp1[i - 1] - prices[i])
            dp3[i] = dp2[i - 1] + prices[i]

        return max(dp1[-1], dp3[-1])
