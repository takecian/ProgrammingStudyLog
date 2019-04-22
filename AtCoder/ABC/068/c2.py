# https://atcoder.jp/contests/abc068/tasks/arc079_a

import itertools
import collections
import bisect

def main():
    N, M = map(int, input().split())

    src = {}
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

        if a == 1:
            src[b] = 1

    for i in range(M):
        if A[i] in src and B[i] == N:
            print("POSSIBLE")
            exit()

    print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
