# https://atcoder.jp/contests/abc127/tasks/abc127_e

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

# Calculate count of combination
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

    com = combination(N * M - 2, K - 2)
    # print(com)
    com = com % MOD
    # print(com)

    ans = 0
    for i in range(N*M):
        iy = i // M
        ix = i % M
        # x
        left = min(0, ix - 1)
        left_sum = left * (left + 1) // 2 * M

        right = M - ix
        right_sum = right * (right + 1) // 2 * M

        # y
        top = min(0, iy - 1)
        top_sum = top * (top + 1) // 2 * N

        bottom = N - iy
        bottom_sum = bottom * (bottom + 1) // 2 * N
        ans += (left_sum + right_sum + top_sum + bottom_sum) * com
        ans = ans % MOD

    print(ans)



if __name__ == '__main__':
    main()
