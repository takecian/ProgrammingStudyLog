# https://atcoder.jp/contests/abc076/tasks/abc076_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    K = int(input())

    val = 1
    for _ in range(N):
        val = min(val * 2, val + K)
    print(val)

if __name__ == '__main__':
    main()
