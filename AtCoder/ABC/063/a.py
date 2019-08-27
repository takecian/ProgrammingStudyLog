
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
    print(a + b if a + b < 10 else 'error')

if __name__ == '__main__':
    main()
