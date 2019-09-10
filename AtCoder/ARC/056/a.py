import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b, k, l = map(int, input().split())
    b_times = k // l
    rest = k % l
    print(b_times * b + min(a * rest, b))


if __name__ == '__main__':
    main()
