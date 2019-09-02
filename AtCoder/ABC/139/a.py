#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    sl = input()
    tl = input()
    ans = 0
    for s, t in zip(sl, tl):
        if s == t:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
