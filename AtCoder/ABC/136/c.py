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

    if n == 1:
        print('Yes')
        return

    prev = None
    hl.reverse()
    for i in range(1, len(hl)):
        if hl[i-1] < hl[i]: # 減少したらダメ
            if hl[i-1] == hl[i] - 1:
                hl[i] = hl[i] - 1
            else:
                print('No')
                return
        else:
            continue

    print('Yes')
    return

if __name__ == '__main__':
    main()
