#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    a, b = map(int, input().split())
    print(max(a+b,a-b,a*b))

if __name__ == '__main__':
    main()
