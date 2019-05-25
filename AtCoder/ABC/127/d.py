# https://atcoder.jp/contests/abc127/tasks/abc127_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    changes = []
    for _ in range(M):
        b, c = map(int, input().split())
        changes.append((b, c))

    A.sort()
    changes.sort(key=lambda x: x[1], reverse=True)
    # print(A)
    # print(changes)

    ai = 0
    for b, c in changes:
        if A[ai] > c:
            break
        for _ in range(b):
            if A[ai] > c:
                break
            if A[ai] < c:
                A[ai] = c
                ai += 1

                if ai >= len(A):
                    break

        if ai >= len(A):
            break
    print(sum(A))


if __name__ == '__main__':
    main()
