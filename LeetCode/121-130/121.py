# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline


class Solution:
    def maxProfit(self, prices) -> int:
        # big value
        INF = int(1e15)
        ans = 0
        min_val = INF
        for p in prices:
            min_val = min(min_val, p)
            ans = max(ans, p - min_val)
        return ans


def main():
    s = Solution()
    print(s.maxProfit([7,6,4,3,1]))


if __name__ == '__main__':
    main()
