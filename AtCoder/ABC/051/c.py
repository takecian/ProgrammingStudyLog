import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    sx, sy, tx ,ty  = map(int, input().split())
    dx = tx - sx
    dy = ty - sy

    p1 = 'R' * dx + 'U' * dy
    p2 = 'L' * dx + 'D' * dy
    p3 = 'D' + 'R' * (dx + 1) + 'U' * (dy + 1) + 'L'
    p4 = 'U' + 'L' * (dx + 1) + 'D' * (dy + 1) + 'R'
    print(p1 + p2 + p3 + p4)


if __name__ == '__main__':
    main()
