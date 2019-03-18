# https://codeforces.com/contest/1136/problem/A

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    l = []
    for _ in range(N):
        f, e = map(int, input().split())
        l.append(e)
    m = int(input())

    ans = 0
    for e in l:
        if m <= e:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
