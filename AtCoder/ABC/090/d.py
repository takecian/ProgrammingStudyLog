# https://atcoder.jp/contests/abc090/tasks/arc091_b

import itertools
import collections
import bisect


def main():
    N, K = map(int, input().split())
    ans = 0
    for b in range(K+1, N+1):
        p = N // b
        r = N - b * p
        tmp = p * (b - K) + max(0, r - K + 1)
        # print("b = {}, c = {}, p = {}, tmp = {}".format(b, b - K, p, tmp))
        ans += tmp

    if K == 0:
        ans -= N

    print(ans)


if __name__ == '__main__':
    main()
