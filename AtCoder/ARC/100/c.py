# https://atcoder.jp/contests/arc100/tasks/arc100_a


import itertools
import collections
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))

    D = []
    for i in range(len(A)):
        D.append(A[i] - (i + 1))
    print(D)
    D.sort()
    print(D)
    mid = D[N/2]
    print()


if __name__ == '__main__':
    main()
