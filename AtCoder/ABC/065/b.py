# https://atcoder.jp/contests/abc065/tasks/abc065_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]

    ans = 0
    i = 0
    for _ in range(N):
        if a[i] - 1 == 1:
            print(ans + 1)
            exit()
        i = a[i] - 1
        ans += 1

    print(-1)

if __name__ == '__main__':
    main()
