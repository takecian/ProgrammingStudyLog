# https://atcoder.jp/contests/abc144/tasks/abc144_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
        return

    print(a * b)

if __name__ == '__main__':
    main()
