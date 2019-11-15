import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, k = map(int, input().split())
    hl = list(map(int, input().split()))
    print(len(list(filter(lambda h: h >= k, hl))))


if __name__ == '__main__':
    main()
