# https://atcoder.jp/contests/abc156/tasks/abc156_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, r = map(int, input().split())
    print(r + max(0, 100 * (10 - n)))


if __name__ == '__main__':
    main()
