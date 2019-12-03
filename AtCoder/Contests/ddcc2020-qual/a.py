# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_a

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    x, y = map(int, input().split())

    ans = 0
    for rank in [x, y]:
        if rank == 1:
            ans += 300000
        if rank == 2:
            ans += 200000
        if rank == 3:
            ans += 100000
    if x == 1 and y == 1:
        ans += 400000

    print(ans)


if __name__ == '__main__':
    main()
