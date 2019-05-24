# https://atcoder.jp/contests/abc066/tasks/arc077_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    n = int(input())
    a = list(map(int, input().split()))

    i = len(a) - 1
    while i >= 0:
        print(a[i], end=" ")
        i -= 2

    i = 1 if i == -2 else 0
    while i < len(a):
        print(a[i], end=" ")
        i += 2


if __name__ == '__main__':
    main()
