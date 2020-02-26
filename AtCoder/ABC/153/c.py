# https://atcoder.jp/contests/abc153/tasks/abc153_c
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, k = map(int, input().split())
    hl = list(map(int, input().split()))
    hl.sort()
    rest = max(0, n-k)
    hl = hl[:rest]
    print(sum(hl))
    return


if __name__ == '__main__':
    main()
