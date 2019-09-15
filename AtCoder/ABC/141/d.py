#
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop, heapify


def main():
    n, m = map(int, input().split())
    al = list(map(int, input().split()))
    for i in range(len(al)):
        al[i] = -al[i]

    heapify(al)

    for _ in range(m):
        val = heappop(al)
        val *= -1
        val //= 2
        val *= -1

        heappush(al, val)

    print(-sum(al))


if __name__ == '__main__':
    main()
