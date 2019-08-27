#

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def f(x):
    y = 1
    e = 1
    if x == 1:
        return False

    while True:
        e *= 4
        y += e
        if x <= y:
            return True
        y += e
        if x <= y:
            return False


def main():
    n = int(input())

    print('Takahashi' if f(n) else 'Aoki')


if __name__ == '__main__':
    main()
