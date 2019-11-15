import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s = input()
    zero = s.count('0')
    one = s.count('1')
    print(min(zero, one) * 2)


if __name__ == '__main__':
    main()
