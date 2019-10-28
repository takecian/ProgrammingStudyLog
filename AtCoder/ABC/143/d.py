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
    ll = list(map(int, input().split()))
    ll.sort()

    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            rest = ll[j + 1:]
            a_plus_b = ll[i] + ll[j]
            pos_right = bisect.bisect_left(rest, a_plus_b)
            count = pos_right

            ans += count
    print(ans)


if __name__ == '__main__':
    main()
