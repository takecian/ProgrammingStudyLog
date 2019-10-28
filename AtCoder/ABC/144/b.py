# https://atcoder.jp/contests/abc144/tasks/abc144_b
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
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()
