#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    x = int(input())
    div = x // 11
    mod = x % 11
    if mod == 0:
        add = 0
    elif mod < 7:
        add = 1
    else:
        add = 2
    print(div * 2 + add)


if __name__ == '__main__':
    main()
