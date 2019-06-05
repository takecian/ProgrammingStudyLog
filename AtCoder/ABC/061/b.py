# https://atcoder.jp/contests/abc061/tasks/abc061_b

import itertools
import collections
import bisect

def main():
    N, M = map(int, input().split())
    ans = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        ans[a-1] += 1
        ans[b-1] += 1
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
