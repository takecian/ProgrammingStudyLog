# https://atcoder.jp/contests/abc090/tasks/arc091_a

import itertools
import collections
import bisect

def main():
    N, M = map(int, input().split())
    if N > 1 and M > 1:
        print((N-2)*(M-2))
    else:
        if N == 1 and M == 1:
            print(1)
        else:
            print(max(N, M) - 2)


if __name__ == '__main__':
    main()
