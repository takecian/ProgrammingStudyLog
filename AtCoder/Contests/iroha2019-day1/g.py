# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_g

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    if math.ceil(N / K) > M:
        print(-1)
        exit()

    # dp[i][j] -- i日目にj回好意をほのめかした時の最大値
    dp = [[0] * (M + 1) for _ in range(N+1)]

    for i in range(N):
        for k in range(K):
            if i + k >= N:
                break
            for j in range(M):
                if i < j:
                    continue
                # print('i = {}, j = {}, k = {}'.format(i, j, k))
                dp[i + k + 1][j + 1] = max(dp[i + k + 1][j + 1], dp[i][j] + A[i])

    # print(dp)
    print(dp[N][M])



if __name__ == '__main__':
    main()
