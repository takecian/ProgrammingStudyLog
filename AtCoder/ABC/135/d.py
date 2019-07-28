#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    mod = 10 ** 9 + 7
    s = list(input())
    n = len(s)
    s.reverse()

    dp = [[0] * 13 for _ in range(n + 1)]
    dp[0][0] = 1

    mul = 1
    for i, c in enumerate(s):  # 桁の小さい方から調べる
        for j in range(10):
            if (c.isdigit() and int(c) == j) or c == '?':
                m = (j * mul) % 13  # その桁での余り
                for k in range(13):   # 一つ前の桁まででの余りの数を元に、その桁を含めた数の余りを出すパターン数を計算する
                    dp[i + 1][(m + k) % 13] += dp[i][k]
        for k in range(13):
            dp[i + 1][k] = dp[i + 1][k] % mod
        mul *= 10
        mul %= 13
    print(dp[n][5])


if __name__ == '__main__':
    main()
