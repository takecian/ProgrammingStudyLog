#

#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    al = [int(input()) for _ in range(n)]

    lsbs = deque()
    for a in al:
        pos = bisect.bisect_left(lsbs, a)
        if pos == 0:
            lsbs.appendleft(a)
        else:
            if pos == len(lsbs):
                lsbs[-1] = a
            else:
                lsbs[pos-1] = a
        # print(lsbs)
    print(len(lsbs))


if __name__ == '__main__':
    main()
