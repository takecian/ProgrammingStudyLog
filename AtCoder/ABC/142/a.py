# https://atcoder.jp/contests/abc142/tasks/abc142_a
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
    odd = n - n // 2
    print(odd/n)

if __name__ == '__main__':
    main()
