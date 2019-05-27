# https://atcoder.jp/contests/abc127/tasks/abc127_e

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

# Calculate count of combination
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def combination(n, r):
    if r == 0:
        return 1
    a = 1
    b = 1
    for i in range(r):
        a *= (n - i)
        if a % (i + 1):
            a //= (i + 1)
        else:
            b *= (i + 1)
    return a // b


def main():
    MOD = 10**9 + 7
    N, M, K = map(int, input().split())

    pattern = cmb(N * M - 2, K - 2)
    # print(com)
    pattern = pattern % MOD
    # print(com)

    ans = 0

    for dx in range(1, M):
        ans += dx * (M - dx) * pattern * (N * N)
        ans = ans % MOD

    # y
    for dy in range(1, N):
        ans += dy * (N - dy) * pattern * (M * M)
        ans = ans % MOD

    ans = ans % MOD
    print(ans)


if __name__ == '__main__':
    main()
