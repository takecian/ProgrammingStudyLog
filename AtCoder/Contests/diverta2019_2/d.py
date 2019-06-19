# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


def main():
    N = int(input())
    ga, sa, ba = map(int, input().split())
    gb, sb, bb = map(int, input().split())

    # n = exchange(N, [ga, sa, ba], [gb, sb, bb])
    # exit()

    dp1 = [0] * (N + 1)

    # A で交換して B で全部どんぐりに戻す
    for i in range(1, N + 1):
        dp1[i] = max(dp1[i - 1] + 1,
                     (dp1[i - ga] + gb) if i - ga >= 0 else 0,
                     (dp1[i - sa] + sb) if i - sa >= 0 else 0,
                     (dp1[i - ba] + bb) if i - ba >= 0 else 0)
        # print(dp1)

    N2 = dp1[N]
    dp2 = [0] * (N2 + 1)

    # B で交換して A で全部どんぐりに戻す
    for i in range(1, N2 + 1):
        dp2[i] = max(dp2[i - 1] + 1,
                     (dp2[i - gb] + ga) if i - gb >= 0 else 0,
                     (dp2[i - sb] + sa) if i - sb >= 0 else 0,
                     (dp2[i - bb] + ba) if i - bb >= 0 else 0)
        # print(dp2)

    print(dp2[N2])


if __name__ == '__main__':
    main()
