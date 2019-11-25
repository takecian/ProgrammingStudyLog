import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b, x = map(int, input().split())

    ans = 0
    l = 1
    r = 10 ** 9
    while l <= r:
        m = (l + r) // 2
        digit = len(str(m))
        price = a * m + b * digit
        # print(l, r,price)
        if price <= x:
            ans = max(ans, m)
        if x < price:
            r = m - 1
        else:
            l = m + 1

    print(ans)


if __name__ == '__main__':
    main()
