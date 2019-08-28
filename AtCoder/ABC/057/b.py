# https://atcoder.jp/contests/abc057/tasks/abc057_b

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, m = map(int, input().split())

    abl = []
    for _ in range(n):
        a, b = map(int, input().split())
        abl.append((a,b))

    cdl = []
    for i in range(m):
        c, d = map(int, input().split())
        cdl.append((c, d, i))

    for a,b in abl:
        checkpoints = sorted(cdl, key=lambda cd: abs(a - cd[0]) + abs(b - cd[1]))
        print(checkpoints[0][2] + 1)


if __name__ == '__main__':
    main()
