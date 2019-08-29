class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(d)]
        for i in range(1, f+1):
            if i < target + 1:
                dp[0][i] = 1
        # print(dp)
        for dice in range(1,d):
            for v in range(1, target + 1):
                for face in range(1, f+1):
                    # print('{} {} {}'.format(dice, v, face))
                    if v + face < target + 1:
                        dp[dice][v + face] += dp[dice-1][v]
        return dp[-1][target] % mod