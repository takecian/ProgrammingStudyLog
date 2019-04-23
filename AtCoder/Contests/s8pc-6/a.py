# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_a

import itertools
import collections
import bisect
import math

def main():
    N, T  = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    print(math.ceil(total / T))

if __name__ == '__main__':
    main()
