# https://atcoder.jp/contests/abc153/tasks/abc153_b
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    h, n = map(int, input().split())
    al = list(map(int, input().split()))
    print('Yes' if h <= sum(al) else 'No')
    return


if __name__ == '__main__':
    main()
