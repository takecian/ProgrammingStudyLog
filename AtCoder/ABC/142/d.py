import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def primes(n):
    pl = [1]
    if n == 2:
        pl.append(2)
        return pl
    if n == 3:
        pl.append(3)
        return pl

    i = 2
    while i * i <= n:
        if n % i == 0:
            pl.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        pl.append(n)
    return pl


def main():
    a, b = map(int, input().split())
    ap = set(primes(a))
    bp = set(primes(b))
    # print(ap)
    # print(bp)
    # print(ap & bp)
    print(len(ap & bp))


if __name__ == '__main__':
    main()
