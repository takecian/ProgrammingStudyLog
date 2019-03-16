# https://atcoder.jp/contests/agc020/tasks/agc020_a

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())

    diff = B - A
    if diff % 2 == 1:
        print("Borys")
    else:
        print("Alice")


if __name__ == '__main__':
    main()
