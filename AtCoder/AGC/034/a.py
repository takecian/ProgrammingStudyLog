# https://atcoder.jp/contests/agc034/tasks/agc034_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N, A, B, C, D = map(int, input().split())
    S = list(input())

    blocks = 0
    for s in range(A - 1, C):
        if S[s] == '.':
            if blocks > 1:
                print('No')
                exit()
            blocks = 0
        else:
            blocks += 1

    blocks = 0
    for s in range(B - 1, D):
        if S[s] == '.':
            if blocks > 1:
                print('No')
                exit()
            blocks = 0
        else:
            blocks += 1

    if D < C:  # 追い越す場所が必要
        can_overtake = False
        for s in range(B - 1, D):
            if S[s-1] == '.' and S[s] == '.' and S[s+1] == '.':
                can_overtake = True
                break

        if not can_overtake:
            print('No')
            exit()

    print('Yes')


if __name__ == '__main__':
    main()
