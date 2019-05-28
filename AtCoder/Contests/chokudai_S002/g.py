# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_g

import itertools
import collections
import bisect

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


def main():
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(gcd(a, b))

if __name__ == '__main__':
    main()
