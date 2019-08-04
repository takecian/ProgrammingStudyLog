#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    ans = 0
    if n < 10:
        print(n)
        return

    ans = 9  # 1-9
    if n < 100:
        print(ans)
        return

    if n < 1000:
        ans += (n - 100 + 1)
        print(ans)
        return
    ans += 900  # 100-999

    if n < 10000:
        print(ans)
        return

    if n < 100000:
        ans += (n - 10000 + 1)
        print(ans)
        return
    ans += 90000  # 10000-99999

    print(ans)

if __name__ == '__main__':
    main()
