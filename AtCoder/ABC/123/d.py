# https://atcoder.jp/contests/abc123/tasks/abc123_d

import itertools
import collections
import bisect

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)

    AB.sort(reverse=True)
    AB = AB[:K]
    # print(A)
    # print(B)
    # print(AB)

    ans = []
    for ab in AB:
        for c in C:
            ans.append(ab + c)

    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])


if __name__ == '__main__':
    main()
