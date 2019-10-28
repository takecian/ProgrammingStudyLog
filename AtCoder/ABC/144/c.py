# https://atcoder.jp/contests/abc144/tasks/abc144_c
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
import math
from heapq import heappush, heappop, heapify


def main():
    n = int(input())

    v = 1
    while v * v <= n:
        v += 1

    for i in range(v, 0, -1):
        if n % i == 0:
            j = n // i
            print(i + j - 2)
            return


if __name__ == '__main__':
    main()
