# https://atcoder.jp/contests/abc079/tasks/abc079_b

import itertools
import collections
import bisect

def main():
    N = int(input())

    L = [0] * 90
    L[0] = 2
    L[1] = 1
    for i in range(2, 87):
        L[i] = L[i-1] + L[i-2]
    print(L[N])


if __name__ == '__main__':
    main()
