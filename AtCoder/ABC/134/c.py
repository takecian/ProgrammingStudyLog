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
    a = [int(input()) for _ in range(n)]
    sort_a = sorted(a)

    for v in a:
        if v == sort_a[-1]:
            print(sort_a[-2])
        else:
            print(sort_a[-1])


if __name__ == '__main__':
    main()
