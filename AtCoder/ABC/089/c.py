# https://atcoder.jp/contests/abc089/tasks/abc089_c

import itertools
import collections
import bisect

def main():
    N = int(input())
    A = {}
    for key in ['M', 'A', 'R', 'C', 'H']:
        A[key] = []
    for _ in range(N):
        a = input()
        if a[0] in ['M', 'A', 'R', 'C', 'H']:
            A[a[0]].append(a)

    # print(A)
    ans = 0

    for c in itertools.combinations(['M', 'A', 'R', 'C', 'H'], 3):
        ans += len(A[c[0]]) * len(A[c[1]]) * len(A[c[2]])

    print(ans)


if __name__ == '__main__':
    main()
