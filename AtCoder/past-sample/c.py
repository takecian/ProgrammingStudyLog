import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    N, T = map(int, input().split())
    ans = 10000
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)

    print(ans if ans != 10000 else 'TLE')


if __name__ == '__main__':
    main()
