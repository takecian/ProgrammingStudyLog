
# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n, k = map(int, input().split())
    al = list(map(int, input().split()))
    down1 = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if al[i] > al[j]:
                down1 += 1

    down2 = 0
    for i in range(n):
        for j in range(n):
            if al[i] > al[j]:
                down2 += 1

    mod = 10**9 + 7
    print((down1 * k + down2 * k * (k - 1) // 2) % mod)


if __name__ == '__main__':
    main()
