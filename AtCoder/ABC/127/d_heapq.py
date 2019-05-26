# https://atcoder.jp/contests/abc127/tasks/abc127_d


import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    changes = []
    for _ in range(M):
        b, c = map(int, input().split())
        changes.append((b, c))


if __name__ == '__main__':
    main()
