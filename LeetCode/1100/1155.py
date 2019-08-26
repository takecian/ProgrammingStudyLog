class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10 ** 9 + 7

        dp = [[0] * 1001 for _ in range(d)]
        for i in range(f):
            dp[0][i + 1] = 1

        for dice in range(1, d):
            for val in range(1001):
                for face in range(1, f + 1):
                    if val + face < 1001:
                        dp[dice][val + face] += (dp[dice - 1][val] % modulo)
        return dp[-1][target] % modulo