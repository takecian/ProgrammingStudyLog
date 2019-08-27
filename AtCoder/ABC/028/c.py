#

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b, c, d, e = map(int, input().split())
    print(max(a+d+e,b+c+e))


if __name__ == '__main__':
    main()
