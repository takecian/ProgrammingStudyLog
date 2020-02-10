# https://atcoder.jp/contests/abc152/tasks/abc152_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, m = map(int, input().split())
    print('Yes' if n == m else 'No')

if __name__ == '__main__':
    main()
