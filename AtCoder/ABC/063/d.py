# https://atcoder.jp/contests/abc063/tasks/arc075_b
import sys
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
import math
sys.setrecursionlimit(12345678)


def can_delete(ml, t, a, b):
    for i in range(len(ml)):
        ml[i] -= (b * t)

    count = 0
    for m in ml:
        if m > 0:
            count += math.ceil(m/(a-b))

    return t >= count


def main():
    n, a, b = map(int, input().split())
    monsters = []
    for _ in range(n):
        monsters.append(int(input()))

    l = 0
    r = 10**9
    while l < r:
        m = (l + r) // 2
        if can_delete(monsters[:], m, a, b):
            r = m
        else:
            l = m + 1

    print(r)


if __name__ == '__main__':
    main()
