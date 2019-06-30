#
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(1, n - 1):
        if p[i+1] < p[i] < p[i-1] or p[i-1] < p[i] < p[i+1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
