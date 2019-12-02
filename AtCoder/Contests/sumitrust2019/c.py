# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    x = int(input())
    dp = [False] * (100000 + 1)
    dp[0] = True

    for p in [100,101,102,103,104,105]:
        for i in range(100000 + 1):
            if p <= i:
                dp[i] |= dp[i-p]

    print(1 if dp[x] else 0)


if __name__ == '__main__':
    main()
