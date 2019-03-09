# https://atcoder.jp/contests/abc089/tasks/abc089_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    S = input().split()
    print("Four" if S.count("Y") else "Three")

if __name__ == '__main__':
    main()
