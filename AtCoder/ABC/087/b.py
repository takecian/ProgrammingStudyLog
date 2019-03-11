# https://atcoder.jp/contests/abc087/tasks/abc087_b

import itertools
import collections
import bisect

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    ans = 0
    for a in range(A+1):
        for b in range(B+1):
            rest = X - 500 * a - 100 * b
            if 0 <= rest <= 50 * C:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
