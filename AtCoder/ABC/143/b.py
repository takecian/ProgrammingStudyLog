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
    n = int(input())
    dl = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            ans += dl[i] * dl[j]
    print(ans)

if __name__ == '__main__':
    main()
