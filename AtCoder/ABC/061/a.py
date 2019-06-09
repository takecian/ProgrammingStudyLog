# https://atcoder.jp/contests/abc061/tasks/abc061_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    A, B, C = map(int, input().split())
    print('Yes' if A <= C <= B else "No")

if __name__ == '__main__':
    main()
