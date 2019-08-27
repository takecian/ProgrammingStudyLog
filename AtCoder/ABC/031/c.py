# https://atcoder.jp/contests/abc031/tasks/abc031_c
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

    ans = -10**10
    for t in range(n):
        aoki_score = -10**10
        takahashi_score = -10**10
        for a in range(n):
            if a == t:
                continue
            l = min(t, a)
            r = max(t, a)
            bl = al[l:(r+1)]
            # print(bl[1::2])
            temp_aoki = sum(bl[1::2])
            temp_takahashi = sum(bl[::2])
            if aoki_score < temp_aoki:
                aoki_score = temp_aoki
                takahashi_score = temp_takahashi
        ans = max(ans, takahashi_score)

    print(ans)


if __name__ == '__main__':
    main()
