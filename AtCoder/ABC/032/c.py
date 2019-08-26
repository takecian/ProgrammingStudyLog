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
    sl = [int(input()) for _ in range(n)]

    if min(sl) == 0:
        print(n)
        return

    if k < min(sl):
        print(0)
        return

    l = 0
    val = 1
    ans = 0
    for r in range(n):
        val *= sl[r]
        if k < val:
            while k < val and l < r:
                val //= sl[l]
                l += 1

        if val <= k:
            ans = max(ans, r - l + 1)

    print(ans)


if __name__ == '__main__':
    main()
