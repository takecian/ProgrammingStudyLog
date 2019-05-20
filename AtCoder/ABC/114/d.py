# https://atcoder.jp/contests/abc114/tasks/abc114_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    primes = [0] * (N + 1)

    for i in range(N + 1):
        cur = i
        for j in range(2, i + 1):
            while cur % j == 0:
                primes[j] += 1
                cur //= j

    ans = 0
    for i in range(2, N - 1):
        for j in range(i + 1, N):
            for k in range(j + 1, N + 1):
                # 75
                if (i == 75 and j == 0 and k == 0) or (i == 0 and j == 75 and k == 0) or (i == 0 and j == 0 and k == 75):
                    ans += 1
                else:
                    if (i == 15 and j == 5 and k == 0) or (i == 0 and j == 15 and k == 0) or (i == 0 and j == 0 and k == 75):
                # 15, 5


if __name__ == '__main__':
    main()
