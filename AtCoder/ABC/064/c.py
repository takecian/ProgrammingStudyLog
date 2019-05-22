# https://atcoder.jp/contests/abc064/tasks/abc064_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ratings = [0] * 9
    for a in A:
        ratings[min(a // 400, 8)] += 1

    # print(ratings)

    fixed_colors = 0
    for r in range(len(ratings) - 1):
        if ratings[r] > 0:
            fixed_colors += 1

    everything_ok = ratings[-1]

    min_colors = fixed_colors if fixed_colors > 0 else 1
    max_colors = fixed_colors + everything_ok
    print('{} {}'.format(min_colors, max_colors))


if __name__ == '__main__':
    main()
