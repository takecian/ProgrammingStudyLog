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
    dl = set(map(int, input().split()))

    for i in range(n, 100000):
        if i < n:
            continue
        candi = list(map(int, list(str(i))))
        available = True
        for c in candi:
            if c in dl:
                available = False
                break
        if available:
            print(i)
            return


if __name__ == '__main__':
    main()
