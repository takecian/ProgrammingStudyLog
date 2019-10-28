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
    s = input()
    ans = 1

    for i in range(1, n):
        if s[i-1] != s[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
