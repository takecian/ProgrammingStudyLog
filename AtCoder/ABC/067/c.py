# https://atcoder.jp/contests/abc067/tasks/arc078_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    INF = int(1e15)
    ans = INF
    acc = 0
    for i in range(len(A) - 1):
        acc += A[i]
        ans = min(ans, abs(total - 2 * acc))

    print(ans)

if __name__ == '__main__':
    main()
