# https://atcoder.jp/contests/abc037/tasks/abc037_c

import itertools
import collections
import bisect

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    sums = [0] * (N + 1)
    for i in range(N):
        sums[i+1] = sums[i] + A[i]

    ans = 0
    # print(sums)
    for i in range(K, N + 1):
        ans += (sums[i] - sums[i - K])

    print(ans)

if __name__ == '__main__':
    main()
