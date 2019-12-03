# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_b

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n = int(input())
    al = list(map(int, input().split()))

    cum_len = [0] * len(al)
    cum_len[0] = al[0]
    for i in range(1, len(al)):
        cum_len[i] = cum_len[i-1] + al[i]

    # print(sum(al))
    ans = 10**10
    for i in range(len(al)):
        left = cum_len[i]
        right = cum_len[-1] - cum_len[i]
        # print(left, right)
        ans = min(ans, abs(left - right))

    print(ans)


if __name__ == '__main__':
    main()
