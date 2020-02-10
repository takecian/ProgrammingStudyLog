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
    alist = list(map(int, input().split()))
    aset = set(alist)
    print('YES' if len(alist) == len(aset) else 'NO')


if __name__ == '__main__':
    main()
