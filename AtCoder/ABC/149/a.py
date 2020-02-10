import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s, t = input().split()
    print(t + s)

if __name__ == '__main__':
    main()
