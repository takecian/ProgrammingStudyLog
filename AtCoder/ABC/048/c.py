# https://atcoder.jp/contests/abc048/tasks/arc064_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, x = map(int, input().split())
    al = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if al[i] + al[i+1] > x:
            dec = (al[i] + al[i+1]) - x
            ans += dec
            al[i+1] = max(0, al[i+1] - dec)

    # print(al)
    print(ans)


if __name__ == '__main__':
    main()
