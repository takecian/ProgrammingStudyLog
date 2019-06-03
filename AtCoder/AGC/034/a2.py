# https://atcoder.jp/contests/agc034/tasks/agc034_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N, A, B, C, D = map(int, input().split())
    S = input()

    ans = 'Yes'
    if '##' in S[A-1:C] or '##' in S[B-1:D]:
        ans = 'No'

    if D < C:  # 追い越す場所が必要
        if '...' not in S[B-2:D+1]:
            ans = 'No'

    print(ans)


if __name__ == '__main__':
    main()
