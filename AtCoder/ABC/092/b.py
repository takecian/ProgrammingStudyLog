# https://atcoder.jp/contests/abc092/tasks/abc092_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    D, X = map(int, input().split())
    choco = 0
    for _ in range(N):
        a = int(input())
        choco += (D - 1) // a + 1
    print(choco + X)


if __name__ == '__main__':
    main()
