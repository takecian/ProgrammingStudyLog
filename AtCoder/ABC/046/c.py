
# https://atcoder.jp/contests/abc046/tasks/arc062_a

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
import math


def main():
    n = int(input())
    t, a = 1, 1
    for _ in range(n):
        tt, at = map(int, input().split())

        temp_t = math.ceil(t/tt)
        temp_a = math.ceil(a/at)
        co = max(temp_t, temp_a)

        t = co * tt
        a = co * at

    print(t + a)

if __name__ == '__main__':
    main()
