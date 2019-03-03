# https://atcoder.jp/contests/abc094/tasks/arc095_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    n = A[-1]
    pos = bisect.bisect(A, n//2)
    if n == A[pos]:
        r = A[pos-1]
    elif pos == 0:
        r = A[pos]
    else:
        r = A[pos] if abs(n/2-A[pos]) < abs(n/2-A[pos-1]) else A[pos-1]

    print("{} {}".format(n, r))


if __name__ == '__main__':
    main()
