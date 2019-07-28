#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        rest = b[i] - a[i]
        if rest > 0:
            ans += min(a[i+1], rest)
            a[i+1] = max(a[i+1] - rest, 0)

    print(ans)


if __name__ == '__main__':
    main()
