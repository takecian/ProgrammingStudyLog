import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, k = map(int, input().split())
    s = input()

    happy = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            happy += 1
    print(min(happy + k * 2, n - 1))

if __name__ == '__main__':
    main()
