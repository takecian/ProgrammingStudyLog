# https://atcoder.jp/contests/abc027/tasks/abc027_b

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    al = list(map(int, input().split()))
    if sum(al) % n != 0:
        print(-1)
        return

    citizens = sum(al) // n
    separated = 0
    gp = 0
    cum = 0
    for i in range(n):
        cum += al[i]
        gp += 1
        if cum / gp == citizens:
            separated += 1
            cum = 0
            gp = 0

    print(n - separated)


if __name__ == '__main__':
    main()
