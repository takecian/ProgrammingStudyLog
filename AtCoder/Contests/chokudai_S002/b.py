# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(a % b)

if __name__ == '__main__':
    main()
