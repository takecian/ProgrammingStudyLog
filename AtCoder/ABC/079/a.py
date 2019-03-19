# https://atcoder.jp/contests/abc079/tasks/abc079_a

import itertools
import collections
import bisect

def main():
    N = list(input())

    if N[1] == N[2] and (N[0] == N[1] or N[2] == N[3]):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
