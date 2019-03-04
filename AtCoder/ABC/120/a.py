# https://atcoder.jp/contests/abc120/tasks/abc120_a

import itertools
import collections
import bisect

def main():
    A, B, C = map(int, input().split())
    print(min(B//A, C))

if __name__ == '__main__':
    main()
