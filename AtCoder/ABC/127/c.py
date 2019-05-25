# https://atcoder.jp/contests/abc127/tasks/abc127_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, M = map(int, input().split())

    max_l = 0
    min_r = 10 ** 6
    for _ in range(M):
        l, r = map(int, input().split())
        max_l = max(max_l, l)
        min_r = min(min_r, r)

    print(max(0, min_r - max_l + 1))

if __name__ == '__main__':
    main()
