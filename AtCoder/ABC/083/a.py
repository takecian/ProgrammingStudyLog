# https://atcoder.jp/contests/abc083/tasks/abc083_a

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    A, B, C, D = map(int, input().split())
    if A + B == C + D:
        print("Balanced")
    else:
        print("Left" if A + B > C + D else "Right")


if __name__ == '__main__':
    main()
