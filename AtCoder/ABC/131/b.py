# https://atcoder.jp/contests/abc131/tasks/abc131_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, L = map(int, input().split())
    apples = [L + i for i in range(N)]
    total = sum(apples)

    rm = 0
    if apples[0] >= 0:
        rm = apples[0]
    else:
        for i in range(N):
            rm = apples[i]
            if rm == 0:
                break
    total -= rm
    print(total)


if __name__ == '__main__':
    main()
