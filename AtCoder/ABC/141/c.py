#
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, k, q = map(int, input().split())
    scores = [k-q] * n
    success = [0] * n
    for _ in range(q):
        a = int(input())
        success[a-1] += 1

    for i in range(n):
        scores[i] += success[i]
        if scores[i] > 0:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
