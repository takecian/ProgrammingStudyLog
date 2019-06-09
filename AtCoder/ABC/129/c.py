#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    MOD = 1000000007

    N, M = map(int, input().split())
    A = set()
    for _ in range(M):
        a = int(input())
        A.add(a)

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i not in A:
            if i == 1:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

    # print(dp)
    ans = dp[N] % MOD
    print(ans)


if __name__ == '__main__':
    main()
