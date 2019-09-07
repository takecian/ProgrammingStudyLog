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
        al[i] -= 1
    bl = list(map(int, input().split()))
    cl = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += bl[al[i]]
        if i > 0:
            if al[i-1] + 1 == al[i]:
                ans += cl[al[i-1]]

    print(ans)


if __name__ == '__main__':
    main()
