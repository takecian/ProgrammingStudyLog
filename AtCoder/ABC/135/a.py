#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    a, b = map(int, input().split())
    if abs(a - b) % 2 == 1:
        print('IMPOSSIBLE')
    else:
        dif = abs(a - b) // 2
        print(min(a,b) + dif)

if __name__ == '__main__':
    main()
