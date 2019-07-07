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
    x = [list(map(int, input().split())) for _ in range(n)]
    # print(x)

    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = 0
            for d1, d2 in zip(x[i], x[j]):
                diff += (d1 - d2) ** 2
            # print(diff)
            diff = math.sqrt(diff)
            if diff == int(diff):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
