# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

import itertools
import collections
import bisect
import statistics
import math

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    a_med = round(statistics.median(A))
    b_med = round(statistics.median(B))

    ans = 0
    for i in range(N):
        ans += abs(B[i] - A[i]) + abs(A[i] - a_med) + abs(B[i] - b_med)
    print(ans)


if __name__ == '__main__':
    main()
