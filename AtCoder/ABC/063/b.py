# https://atcoder.jp/contests/abc063/tasks/abc063_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    S = list(input())
    L = set(S)
    print('yes' if len(S) == len(L) else 'no')

if __name__ == '__main__':
    main()
