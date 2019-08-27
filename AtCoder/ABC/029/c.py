# https://atcoder.jp/contests/abc029/tasks/abc029_c

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

    def rec(txt, c):
        chars = ['a', 'b', 'c']
        if c == 0:
            print(txt)
        else:
            for char in chars:
                rec(txt + char, c - 1)

    rec('', n)


if __name__ == '__main__':
    main()
