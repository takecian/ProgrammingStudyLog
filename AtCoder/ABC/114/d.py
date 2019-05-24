# https://atcoder.jp/contests/abc114/tasks/abc114_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def solve(primes, index, target):
    if index == len(primes):
        if target == 1:
            return 1
        else:
            return 0
    ans = 0
    for i in range(primes[index] + 1):
        if target % (i + 1) != 0:
            continue
        ans += solve(primes, index + 1, target // (i + 1))

    return ans



def main():
    N = int(input())
    primes = [0] * (N + 1)

    for i in range(N + 1):
        cur = i
        for j in range(2, i + 1):
            while cur % j == 0:
                primes[j] += 1
                cur //= j

    # print(primes)
    print(solve(primes, 0, 75))


if __name__ == '__main__':
    main()
