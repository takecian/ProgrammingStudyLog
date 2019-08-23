# https://atcoder.jp/contests/abc040/tasks/abc040_c

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n = int(input())
    al = list(map(int, input().split()))

    cost = [10**10] * n
    cost[0] = 0
    for i in range(n):
        if i + 1 < n:
            cost[i+1] = min(cost[i+1], cost[i] + abs(al[i+1] - al[i]))
        if i + 2 < n:
            cost[i+2] = min(cost[i+2], cost[i] + abs(al[i+2] - al[i]))

    print(cost[-1])


if __name__ == '__main__':
    main()
