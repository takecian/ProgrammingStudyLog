# https://atcoder.jp/contests/abc119/tasks/abc119_d
import itertools
import collections
import bisect

def main():
    # big value
    INF = int(1e15)
    A, B, Q = map(int, input().split())
    S = [-INF] + [int(input()) for _ in range(A)] + [INF]
    T = [-INF] + [int(input()) for _ in range(B)] + [INF]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        pos_s = bisect.bisect(S, x)  # xより大きい S の最小値のインデックス
        pos_t = bisect.bisect(T, x)  # xより大きい T の最小値のインデックス
        s1, s2 = S[pos_s - 1], S[pos_s]
        t1, t2 = T[pos_t - 1], T[pos_t]

        ans = INF
        for st, tt in itertools.product([s1, s2], [t1, t2]):
            path1 = abs(x - st) + abs(st - tt)
            path2 = abs(x - tt) + abs(st - tt)
            ans = min(ans, path1, path2)
        print(ans)

if __name__ == '__main__':
    main()

