# https://atcoder.jp/contests/abc094/tasks/abc094_b

import itertools
import collections
import bisect

def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    pos = bisect.bisect_left(A, X)
    # print(A[:pos])
    # print(A[pos:])
    print(min(len(A[:pos]), len(A[pos:])))


if __name__ == '__main__':
    main()
