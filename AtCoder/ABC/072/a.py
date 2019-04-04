# https://atcoder.jp/contests/abc072/tasks/abc072_a

import itertools
import collections
import bisect

def main():
    X, t = map(int, input().split())
    print(max(0, X - t))

if __name__ == '__main__':
    main()
