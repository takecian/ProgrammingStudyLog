# https://atcoder.jp/contests/abc121/tasks/abc121_b

import itertools
import collections
import bisect

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        s = C
        for a, b in zip(A[i], B):
            s += a * b
        if s > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
