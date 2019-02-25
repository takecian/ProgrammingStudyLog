# https://atcoder.jp/contests/abc119/tasks/abc119_d
import itertools
import collections
import bisect

def main():
    # big value
    INF = int(1e15)
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        pos_s = bisect.bisect(S, x)  # xより小さい S の最大値のインデックス
        pos_t = bisect.bisect(T, x)  # xより大きい T の最大値のインデックス
        s1 = S[pos_s] if pos_s < len(S) else S[pos_s-1]
        s2 = S[pos_s - 1] if pos_s < len(S) else INF


if __name__ == '__main__':
    main()
