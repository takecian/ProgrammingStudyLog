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

    for i in range(n):
        al[i] = (i + 1, al[i])

    al.sort(key=lambda a: -a[1])

    for a in al:
        print(a[0])


if __name__ == '__main__':
    main()
