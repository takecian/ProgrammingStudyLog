# https://atcoder.jp/contests/abc091/tasks/abc091_a


import itertools
import collections
import bisect

def main():
    A, B, C = map(int, input().split())
    print("Yes" if A + B >= C else "No")

if __name__ == '__main__':
    main()
