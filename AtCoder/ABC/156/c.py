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
    xl = list(map(int, input().split()))
    min_p = min(xl)
    max_p = max(xl)
    ans = 10**10
    for p in range(min_p, max_p + 1):
        cost = 0
        for x in xl:
            cost += (x - p) ** 2
        ans = min(ans, cost)

    print(ans)
    return

if __name__ == '__main__':
    main()
