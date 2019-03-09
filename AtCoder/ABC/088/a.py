# https://atcoder.jp/contests/abc088/tasks/abc088_a

import itertools
import collections
import bisect

def main():
    N = int(input())
    A = int(input())
    print("Yes" if N % 500 <= A else "No")

if __name__ == '__main__':
    main()
