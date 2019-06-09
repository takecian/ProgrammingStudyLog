#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10 ** 15
    for i in range(1, N):
        a = sum(W[:i])
        b = sum(W[i:])
        ans = min(ans, abs(a - b))
    print(ans)


if __name__ == '__main__':
    main()
