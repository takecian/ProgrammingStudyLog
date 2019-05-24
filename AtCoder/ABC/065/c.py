# https://atcoder.jp/contests/abc065/tasks/arc076_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N, M = map(int, input().split())

    mod = 10**9 + 7

    if abs(N - M) > 1:
        print(0)
        exit()

    n = 1
    m = 1
    for i in range(1, N + 1):
        n = (n * i) % mod
    for i in range(1, M + 1):
        m = (m * i) % mod

    if N == M:
        print((n * m * 2) % mod)
    else:
        print((n * m) % mod)

if __name__ == '__main__':
    main()
