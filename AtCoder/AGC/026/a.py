# https://atcoder.jp/contests/agc026/tasks/agc026_a

import itertools
import collections
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    prev = -1
    for i in range(N):
        if prev == A[i]:
            count += 1
            A[i] = -1

        prev = A[i]
    print(count)


if __name__ == '__main__':
    main()

