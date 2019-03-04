# https://atcoder.jp/contests/agc021/tasks/agc021_a

import itertools
import collections
import bisect

def main():
    N = list(map(int, input()))
    if N[1:].count(9) == len(N) - 1:
        print(sum(N))
    else:
        print(N[0] - 1 + (len(N) - 1) * 9)


if __name__ == '__main__':
    main()
