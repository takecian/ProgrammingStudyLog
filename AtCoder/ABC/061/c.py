# https://atcoder.jp/contests/abc061/tasks/abc061_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, K = map(int, input().split())
    ab = []
    for _ in range(N):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort(key=lambda x: x[0])

    rest = K
    for a, b in ab:
        if rest <= b:
            print(a)
            exit()
        else:
            rest -= b


if __name__ == '__main__':
    main()
