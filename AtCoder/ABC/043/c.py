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
    al = list(map(int, input().split()))
    ans = 10**15
    for i in range(-100,101):
        y = i
        cost = 0
        for x in al:
            cost += (x - y) ** 2
        ans = min(ans, cost)

    print(ans)


if __name__ == '__main__':
    main()
