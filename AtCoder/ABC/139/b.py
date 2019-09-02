#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    a, b = map(int, input().split())
    ans = 0
    if b == 1:
        print(0)
        return
    count = 1
    while count < b:
        count += (a - 1)
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
