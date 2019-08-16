
#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n, m = map(int, input().split())

    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a,b))

    ab.sort(key=lambda x: x[0])
    # print(ab)
    ans = 0
    j = 0
    h = []
    for i in range(1,m+1):
        while j < len(ab) and ab[j][0] <= i:
            heappush(h, (-ab[j][1]))
            j += 1

        if len(h) > 0:
            val = heappop(h)
            # print(val)
            ans -= val

    print(ans)


if __name__ == '__main__':
    main()
