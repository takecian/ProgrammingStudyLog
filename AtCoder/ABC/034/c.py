# https://atcoder.jp/contests/abc034/tasks/abc034_c
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    W, H = map(int, input().split())
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    mod = 10**9 + 7

    for h in range(H):
        for w in range(W):
            if w + 1 < W:
                dp[h][w+1] += (dp[h][w] % mod)
            if h + 1 < H:
                dp[h+1][w] += (dp[h][w] % mod)
    print(dp[-1][-1] % mod)


if __name__ == '__main__':
    main()
