import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop
import math


def main():
    n = int(input())
    a = [float(input()) for _ in range(n)]

    plus = list(filter(lambda x: x > 0, a))

    all_ceil_p = 0
    absolute_p = 0
    for p in plus:
        if math.floor(p) == math.ceil(p):
            absolute_p += int(p)
        else:
            all_ceil_p += math.floor(p)

    minus = list(filter(lambda x: x < 0, a))

    all_ceil_m = 0
    absolute_m = 0
    for m in minus:
        if math.floor(m) == math.ceil(m):
            absolute_m += int(m)
        else:
            all_ceil_m += math.ceil(m)

    total_p = all_ceil_p + absolute_p
    total_m = all_ceil_m + absolute_m
    count = abs(total_p - abs(total_m))

    if total_p > abs(total_m):  # p is bigger
        for v in a:
            if math.floor(v) == math.ceil(v):
                print(math.ceil(v))
                continue

            if v >= 0:
                print(math.floor(v))
            else:
                if count > 0:
                    print(math.floor(v))
                    count -= 1
                else:
                    print(math.ceil(v))

    else:  # m is bigger
        for v in a:
            if math.floor(v) == math.ceil(v):
                print(math.ceil(v))
                continue

            if v <= 0:
                print(math.ceil(v))
            else:
                if count > 0:
                    print(math.ceil(v))
                    count -= 1
                else:
                    print(math.floor(v))


if __name__ == '__main__':
    main()
