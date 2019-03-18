# https://atcoder.jp/contests/abc082/tasks/abc082_a

import itertools
import collections
import bisect
import math
import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    print(math.ceil((a + b) / 2))

if __name__ == '__main__':
    main()
