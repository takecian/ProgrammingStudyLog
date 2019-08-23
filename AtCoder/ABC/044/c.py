
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, a = map(int, input().split())
    xl = list(map(int, input().split()))
    dp = [[[0] * 2501 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(n):
            for k in range(2501):
                if dp[i][j][k] > 0:
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j + 1][k + xl[i]] += dp[i][j][k]
    ans = 0
    for i in range(1,n+1):
        ans += dp[n][i][i*a]
    print(ans)


if __name__ == '__main__':
    main()
