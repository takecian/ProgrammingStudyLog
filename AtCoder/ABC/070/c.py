# https://abc070.contest.atcoder.jp/tasks/abc070_c

import itertools
import collections
from bisect import bisect


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


def main():
    N = int(input())

    ans = int(input())
    for _ in range(N-1):
        ans = lcm(ans, int(input()))
    print(ans)


if __name__ == '__main__':
    main()
