# https://atcoder.jp/contests/abc039/tasks/abc039_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b, c = map(int, input().split())
    print(2 * (a*b + b*c + a*c))


if __name__ == '__main__':
    main()
