# https://atcoder.jp/contests/abc026/tasks/abc026_b
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
    rl = [int(input()) for _ in range(n)]
    rl.sort(reverse=True)

    ans = 0
    for i in range(len(rl)):
        if i % 2 == 0:
            ans += rl[i] ** 2
        else:
            ans -= rl[i] ** 2

    print(ans * 3.1415926534)

if __name__ == '__main__':
    main()
