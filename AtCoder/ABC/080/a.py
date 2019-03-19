# https://atcoder.jp/contests/abc080/tasks/abc080_a

import itertools
import collections
import bisect

def main():
    N, A, B = map(int, input().split())
    print(min(N * A, B))

if __name__ == '__main__':
    main()
