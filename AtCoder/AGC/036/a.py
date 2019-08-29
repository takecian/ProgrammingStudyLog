# https://atcoder.jp/contests/agc036/tasks/agc036_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    S = int(input())

    y = -(-S // (10 ** 9))
    x = y * (10 ** 9) - S

    print(0, 0, 10 ** 9, 1, x, y)


if __name__ == '__main__':
    main()
