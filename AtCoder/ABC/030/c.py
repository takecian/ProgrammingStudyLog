import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))

    ans = 0

    t = 0
    i = 0
    j = 0
    while i < n and j < m:
        # go
        while i < n:
            if al[i] >= t:
                break
            i += 1

        if i == n:
            break
        t = al[i] + x
        i += 1

        # back
        while j < m:
            if bl[j] >= t:
                break
            j += 1
        if j == m:
            break

        t = bl[j] + y
        j += 1
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
