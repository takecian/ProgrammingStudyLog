# https://atcoder.jp/contests/abc120/tasks/abc120_c

import itertools
import collections
import bisect

def main():
    S = list(input())
    zero_n = S.count("0")
    one_n = S.count("1")
    print(min(zero_n, one_n) * 2)

if __name__ == '__main__':
    main()
