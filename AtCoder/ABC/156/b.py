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
    a = 0
    while n > 0:
        a += 1
        n = n // k

    print(a)
    return


if __name__ == '__main__':
    main()
