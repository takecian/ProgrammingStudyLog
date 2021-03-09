import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    A = [[0 for i in range(3)] for j in range(3)]
    B = [[False for i in range(3)] for j in range(3)]

    for i in range(3):
        line = list(map(int, input().split()))
        A[i][0] = line[0]
        A[i][1] = line[1]
        A[i][2] = line[2]

    N = int(input())
    for i in range(N):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    B[i][j] = True

    # check
    ltor = True
    for i in range(3):
        if not B[i][i]:
            ltor = False
    if ltor:
        print('Yes')
        return

    rtol = True
    for i in range(3):
        if not B[i][2 - i]:
            rtol = False
    if rtol:
        print('Yes')
        return

    for i in range(3):
        if all(B[i]):
            print('Yes')
            return

    for i in range(3):
        if all([B[0][i], B[1][i], B[2][i]]):
            print('Yes')
            return

    print('No')
    return


if __name__ == '__main__':
    main()
