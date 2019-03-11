# https://atcoder.jp/contests/abc087/tasks/arc090_a

import itertools
import collections
import bisect

def main():
    N = int(input())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))

    for i in range(N-1):
        A1[i+1] += A1[i]
    for i in range(N-1, 0, -1):
        A2[i-1] += A2[i]
    # print(A1)
    # print(A2)

    ans = 0
    for i in range(N):
        ans = max(ans, A1[i] + A2[i])
    print(ans)


if __name__ == '__main__':
    main()
