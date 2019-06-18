# https://atcoder.jp/contests/abc060/tasks/abc060_a

import itertools
import collections
import bisect

def main():
    A, B, C = input().split()
    print('YES' if A[-1] == B[0] and B[-1] == C[0] else 'NO')

if __name__ == '__main__':
    main()
