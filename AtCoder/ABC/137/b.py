#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    k, x = map(int, input().split())

    left = x-k+1
    right = x + k
    ans = [i for i in range(left, right)]

    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()
