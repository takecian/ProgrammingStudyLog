# https://atcoder.jp/contests/abc034/tasks/abc034_c
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
from math import factorial


def main():
    w, h = map(int, input().split())
    m = 10 ** 9 + 7
    a = factorial(w + h - 2)
    b = pow(factorial(w - 1), m - 2, m)
    c = pow(factorial(h - 1), m - 2, m)
    print(a * b * c % m)


if __name__ == '__main__':
    main()
