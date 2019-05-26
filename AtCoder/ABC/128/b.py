# https://atcoder.jp/contests/abc128/tasks/abc128_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    reviews = []
    for i in range(N):
        s, p = input().split()
        p = int(p)
        reviews.append((i+1, s, p))

    reviews.sort(key=lambda x: (x[1], -x[2]))
    for r in reviews:
        print(r[0])


if __name__ == '__main__':
    main()
