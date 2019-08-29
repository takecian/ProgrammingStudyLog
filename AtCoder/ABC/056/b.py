import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
# https://atcoder.jp/contests/abc056/tasks/abc056_b

def main():
    w, a, b = map(int, input().split())
    print(max(0, abs(a - b) - w, 0))

if __name__ == '__main__':
    main()
