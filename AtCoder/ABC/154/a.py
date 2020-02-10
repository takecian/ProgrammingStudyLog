import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        a = max(0, a-1)
    else:
        b = max(0, b-1)

    print(a, b)


if __name__ == '__main__':
    main()
