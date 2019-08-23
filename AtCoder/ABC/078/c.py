# https://atcoder.jp/contests/abc078/tasks/arc085_a

import itertools
import collections
import bisect

def main():
    n, m = map(int, input().split())
    print((1900*m+(n-m)*100)*2**m)

if __name__ == '__main__':
    main()
