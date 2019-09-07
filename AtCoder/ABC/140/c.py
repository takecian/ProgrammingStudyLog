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
    bl = list(map(int, input().split()))
    al = [0] * n

    al[0] = bl[0]
    al[-1] = bl[-1]
    for i in range(1, n - 1):
        al[i] = min(bl[i], bl[i-1])
    print(sum(al))


if __name__ == '__main__':
    main()
