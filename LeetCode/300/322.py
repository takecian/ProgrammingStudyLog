# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins, amount):
        inf = 10**10
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1

        print(dp)

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
            print(dp)

        return dp[amount] if dp[amount] < inf else -1


def main():
    s = Solution()
    # print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([1], 0))

if __name__ == '__main__':
    main()
