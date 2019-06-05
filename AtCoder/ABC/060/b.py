# https://atcoder.jp/contests/abc060/tasks/abc060_b

import itertools
import collections
import bisect

def main():
    A, B, C = map(int, input().split())
    for c in range(1, B+1):
        if (A * c) % B == C:
            print('YES')
            exit()

    print('NO')


if __name__ == '__main__':
    main()
