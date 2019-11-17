# https://atcoder.jp/contests/abc145/tasks/abc145_c

import sys
sys.setrecursionlimit(12345678)
import itertools
import math
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n = int(input())
    nl = [i for i in range(n)]

    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))

    total = 0
    routes = list(itertools.permutations(nl))
    for route in routes:
        # print(route)
        distance = 0
        for i in range(1, len(route)):
            src_x = xy[route[i-1]][0]
            src_y = xy[route[i-1]][1]
            dst_x = xy[route[i]][0]
            dst_y = xy[route[i]][1]
            distance += math.sqrt((dst_x - src_x) * (dst_x - src_x) + (dst_y - src_y) * (dst_y - src_y))

        total += distance
    # print(len(routes))
    print(total / len(routes))


if __name__ == '__main__':
    main()
