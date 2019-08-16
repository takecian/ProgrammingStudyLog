#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    sl = []
    for _ in range(n):
        s = list(input())
        s.sort()

        sl.append(''.join(s))

    counter = Counter(sl)
    ans = 0
    for s, c in counter.items():
        if c > 1:
            ptn = c * (c-1) // 2
            ans += ptn
    print(ans)

if __name__ == '__main__':
    main()
