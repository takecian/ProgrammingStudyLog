#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')
    

if __name__ == '__main__':
    main()
