import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    N, M = map(int, input().split())
    cand = [-1] * N

    for i in range(M):
        s, c = map(int, input().split())
        s = s - 1
        if cand[s] == -1:
            cand[s] = c
        elif cand[s] != c:
            print(-1)
            return

    if cand[0] == -1:
        if N > 1:
            cand[0] = 1
        else:
            cand[0] = 0

    for i in range(N):
        if cand[i] == -1:
            cand[i] = 0

    maped_list = map(str, cand)
    ans = int(''.join(maped_list))

    if N == 1:
        print(ans)
    elif ans >= 10 ** (N - 1):
        print(ans)
    else:
        print(-1)

    return

if __name__ == '__main__':
    main()
