#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    vl = list(map(int, input().split()))
    vl.sort()
    while len(vl) > 1:
        val = vl.pop(0)
        vl[0] = (vl[0] + val) / 2

    print(vl[0])

if __name__ == '__main__':
    main()
