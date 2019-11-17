# https://atcoder.jp/contests/abc145/tasks/abc145_b

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
    s = input()
    s1 = s[:n//2]
    s2 = s[n//2:]
    print('Yes' if s1 == s2 else 'No')

if __name__ == '__main__':
    main()
