# https://atcoder.jp/contests/abc075/tasks/abc075_a

import itertools
import collections
import bisect

def main():
    A, B, C = map(int, input().split())
    if A == B:
        print(C)
    if C == B:
        print(A)
    if C == A:
        print(B)

if __name__ == '__main__':
    main()
