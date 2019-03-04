# https://atcoder.jp/contests/abc093/tasks/abc093_a


import itertools
import collections
import bisect

def main():
    S = input()
    if all(c in S for c in ['a', 'b', 'c']):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
