#

#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
import math

def main():
    n, d = map(int, input().split())
    area = d * 2 + 1
    print(math.ceil(n/area))

if __name__ == '__main__':
    main()
