# https://atcoder.jp/contests/abc083/tasks/arc088_a

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    X, Y = map(int, input().split())
    s = X
    ans = 0
    while s <= Y:
        ans += 1
        s *= 2
    print(ans)

if __name__ == '__main__':
    main()
