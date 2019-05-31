# https://atcoder.jp/contests/abc062/tasks/arc074_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    H, W = map(int, input().split())

    # big value
    INF = int(1e15)
    ans = INF

    for h in range(1, H):
        sq1 = h * W

        rest_h = H - h
        # 横で割る   ___
        #           ___
        height1 = rest_h // 2
        height2 = rest_h - height1
        sq2 = height1 * W
        sq3 = height2 * W
        diff = max(sq1, sq2, sq3) - min(sq1, sq2, sq3)
        # print('diff = {}, {} {} {}'.format(diff, sq1, sq2, sq3))
        ans = min(ans, diff)

        # 縦で割る   ___
        #            |
        width1 = W // 2
        width2 = W - width1
        sq2 = width1 * rest_h
        sq3 = width2 * rest_h
        diff = max(sq1, sq2, sq3) - min(sq1, sq2, sq3)
        ans = min(ans, diff)

    for w in range(1, W):
        sq1 = w * H

        rest_w = W - w
        # 縦で割る
        height1 = H // 2
        height2 = H - height1
        sq2 = height1 * rest_w
        sq3 = height2 * rest_w

        diff = max(sq1, sq2, sq3) - min(sq1, sq2, sq3)
        ans = min(ans, diff)

        # 横で割る
        width1 = rest_w // 2
        width2 = rest_w - width1
        sq2 = width1 * H
        sq3 = width2 * H
        diff = max(sq1, sq2, sq3) - min(sq1, sq2, sq3)
        ans = min(ans, diff)


    print(ans)


if __name__ == '__main__':
    main()
