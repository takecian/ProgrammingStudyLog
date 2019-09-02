#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    hl = list(map(int, input().split()))
    counts = [0] * n

    for i in range(1,n):
        if hl[i-1] >= hl[i]:
            counts[i] = counts[i-1] + 1
    # print(counts)
    print(max(counts))


if __name__ == '__main__':
    main()
