import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b, c = map(int, input().split())
    print('bust' if sum([a,b,c]) >= 22 else 'win')

if __name__ == '__main__':
    main()
