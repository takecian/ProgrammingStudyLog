import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    area = abs((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)) / 2
    print(area)


if __name__ == '__main__':
    main()
