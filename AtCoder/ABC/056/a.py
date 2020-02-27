import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b = input().split()
    if a == 'H':
        print(b)
    else:
        if b == 'H':
            print('D')
        else:
            print('H')


if __name__ == '__main__':
    main()
