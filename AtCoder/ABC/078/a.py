# https://atcoder.jp/contests/abc078/tasks/abc078_a

import itertools
import collections
import bisect

def main():
    X, Y = input().split()
    if X == Y:
        print("=")
    else:
        print("<" if X < Y else ">")

if __name__ == '__main__':
    main()
