# https://atcoder.jp/contests/abc131/tasks/abc131_e

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


def output(edges):
    print(len(edges))
    for s, e in edges:
        print('{} {}'.format(s, e))


def main():
    N, K = map(int, input().split())

    edges = []
    # まずグラフを連結させる
    for i in range(2, N + 1):
        edges.append((1, i))

    ma = (N - 1) * (N - 2) // 2
    # print(ma)
    if K > ma:
        print(-1)
        exit()
    rest = ma - K
    cand = []
    for i in range(2, N):
        for j in range(i + 1, N + 1):
            cand.append((i, j))

    # print(rest)
    while rest > 0:
        i, j = cand.pop()
        edges.append((i, j))
        rest -= 1

    output(edges)


if __name__ == '__main__':
    main()
