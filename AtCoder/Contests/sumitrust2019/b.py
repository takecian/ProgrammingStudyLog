# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

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

    for i in range(1, n+1):
        price = int(i * 1.08)
        if price == n:
            print(i)
            return

    print(':(')


if __name__ == '__main__':
    main()
