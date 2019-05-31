# https://atcoder.jp/contests/abc062/tasks/arc074_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    H, W = map(int, input().split())
    if H % 3 == 0 or W % 3 == 0:
        print(0)
        exit()


    # big value
    INF = int(1e15)
    ans = INF
    for h in range(1, H):
        h_sq = h * W
        rest = H - h
        for w in range(1, W // 2 + 1):
            w_sq1 = w * H
            w_sq2 = (W - w) * H
            diff = max(h_sq, w_sq1, w_sq2) - min(h_sq, w_sq1, w_sq2)
            ans = min(ans, diff)

    print(diff)


if __name__ == '__main__':
    main()
