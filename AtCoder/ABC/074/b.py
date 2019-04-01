# https://atcoder.jp/contests/abc074/tasks/abc074_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    K = int(input())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(abs(X[i]), abs(K - X[i])) * 2
    print(ans)


if __name__ == '__main__':
    main()
