# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_g

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

def main():

    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    memo = [[0] * (M + 1) for _ in range(N + 1)]

    def dp(i, j):
        # big value
        INF = int(1e15)
        if j == 0:
            if N <= i + K - 1:
                return 0
            else:
                return -INF

        if memo[i][j] != 0:
            return memo[i][j]
        ret = -INF
        k = 0
        while k < K and i + k < N:
            ret = max(ret, A[i + k] + dp(i + k + 1, j - 1))
            k += 1
        memo[i][j] = ret
        return ret

    print(max(dp(0, M), -1))


if __name__ == '__main__':
    main()
