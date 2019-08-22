# https://atcoder.jp/contests/arc001/tasks/arc001_2

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b = map(int, input().split())
    rest = abs(a - b)
    ans = 0
    ans += rest // 10
    rest = rest % 10

    if rest == 0:
        pass
    elif rest < 4:
        ans += rest
    elif rest == 4 or rest == 6:
        ans += 2
    elif rest == 5:
        ans += 1
    elif rest == 7:
        ans += 3
    elif rest == 8:
        ans += 3
    elif rest == 9:
        ans += 2
    print(ans)


if __name__ == '__main__':
    main()

