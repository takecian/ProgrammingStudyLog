import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    h, a = map(int, input().split())
    if h % a == 0:
        print(h // a)
    else:
        print(h // a + 1)


if __name__ == '__main__':
    main()
