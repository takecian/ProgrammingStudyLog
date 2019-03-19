# https://atcoder.jp/contests/abc088/tasks/abc088_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    a_sum = sum([A[a] for a in range(0, len(A), 2)])
    b_sum = sum([A[a] for a in range(1, len(A), 2)])
    print(a_sum - b_sum)


if __name__ == '__main__':
    main()
