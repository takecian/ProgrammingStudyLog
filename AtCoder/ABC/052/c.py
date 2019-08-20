#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

# 素因数分解
def primes(n):
    ps = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            ps.append(i)
            n //= i
        i += 1
    if n > 1:
        ps.append(n)
    return ps


def main():
    n = int(input())
    pl = []
    for i in range(1,n+1):
        pl += primes(i)

    counter = Counter(pl)
    # print(counter)
    ans = 1
    for v in counter.values():
        ans *= (v + 1)
        ans %= 1000000007
    print(ans)


if __name__ == '__main__':
    main()
