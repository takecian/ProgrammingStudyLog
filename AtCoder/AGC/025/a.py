# https://atcoder.jp/contests/agc025/tasks/agc025_a

import itertools
import collections
import bisect

def main():
    N = int(input())
    if N % 10 == 0:
        print(10)
    else:
        print(sum(map(int, list(str(N)))))


if __name__ == '__main__':
    main()
    