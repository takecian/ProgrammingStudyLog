# https://atcoder.jp/contests/abc094/tasks/abc094_a

import itertools
import collections
import bisect

def main():
    A, B, X = map(int, input().split())
    rest = X - A
    if rest < 0 or rest > B:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()
