#
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

# Calculate count of combination
def combination(n, r):
    a = 1
    b = 1
    for i in range(r):
        a *= (n - i)
        b *= (i + 1)
    return a // b


def main():
    mod = 10 ** 9 + 7
    n, k = map(int, input().split())
    for i in range(1, k + 1):
        ans = combination(n - k + 1, i) * combination(k - 1, i - 1) % mod
        print(ans)


if __name__ == '__main__':
    main()
