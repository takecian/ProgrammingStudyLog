# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline


class Solution:
    def maxProfit(self, prices):
        INF = int(1e15)

        prices.append(-1)

        ans = 0
        buy_p = INF
        sell_p = -1
        for p in prices:
            if sell_p > p:
                ans += max(0, sell_p - buy_p)
                # print("{} - {}".format(sell_p, buy_p))
                buy_p = p
                sell_p = -1
                continue

            buy_p = min(p, buy_p)
            sell_p = max(p, sell_p)

        return ans


def main():
    s = Solution()
    print(s.maxProfit([2,1,2,0,1]))

if __name__ == '__main__':
    main()
