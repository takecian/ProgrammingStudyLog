# https://atcoder.jp/contests/abc080/tasks/abc080_c

import itertools
import collections
import bisect


def main():
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]

    # print(F)
    # print(P)

    # big value
    INF = int(1e15)
    ans = -INF
    pattern = 1024
    for i in range(1, pattern):
        score = 0
        # print(bin(i))
        for s in range(N):
            matched = 0
            f = F[s]
            p = P[s]
            # print(f)
            # print(p)
            for j in range(10):
                if (i >> j) & 1:  # open
                    matched += 1 if f[j] else 0

            # print("s = {} match = {}".format(s, matched))
            score += p[matched]
        # print(score)
        ans = max(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
