# https://atcoder.jp/contests/abc152/tasks/abc152_c
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
    pl = list(map(int, input().split()))
    minv = n + 1
    ans = 0
    for p in pl:
        if minv > p:
            ans += 1
            minv = p
    print(ans)
    return


if __name__ == '__main__':
    main()
