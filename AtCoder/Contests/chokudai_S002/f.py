# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_f

import itertools
import collections
import bisect

def main():
    N = int(input())
    s = set()
    for _ in range(N):
        a, b = map(int, input().split())
        s.add((a,b) if a < b else (b, a))

    print(len(s))


if __name__ == '__main__':
    main()
