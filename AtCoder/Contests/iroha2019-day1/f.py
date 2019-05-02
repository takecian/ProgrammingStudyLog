# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_f

import itertools
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from functools import reduce
import bisect

# 素因数分解
def prime_list(n):
    primes = []

    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            primes.append(i)
        i += 1

    if n > 1:
        primes.append(n)

    return primes


def main():
    N, K = map(int, input().split())

    p = prime_list(N)
    # print(p)
    if len(p) < K:
        print(-1)
    else:
        ans = p[:K-1]
        rest = p[K-1:]
        ans += [reduce(lambda x, y: x * y, rest)]
        print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()
