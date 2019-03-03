# https://atcoder.jp/contests/abc094/tasks/arc095_a

import itertools
import collections
import bisect
import copy

def main():
    N = int(input())
    X = list(map(int, input().split()))
    Y = sorted(X)
    for i in range(N):
        pos = bisect.bisect(Y, X[i])
        if pos <= N//2:
            print(Y[N//2])
        else:
            print(Y[N // 2 - 1])


if __name__ == '__main__':
    main()
    