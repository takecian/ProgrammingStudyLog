# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    m1, d1 = map(int, input().split())
    m2, d2 = map(int, input().split())

    print(1 if d2 == 1 else 0)

if __name__ == '__main__':
    main()
