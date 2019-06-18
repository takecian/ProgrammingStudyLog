
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    P = list(map(int, input().split()))

    # dp[i][j] i 個までの要素の中で、j以下
    # dp[N][K]
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for k in range(1, K + 1):
        for i in range(1, N + 1):
            item_weight = W[i - 1]
            item_price = P[i - 1]
            if item_weight <= k:
                dp[i][k] = max(dp[i-1][k - item_weight] + item_price, dp[i-1][k])
            else:
                dp[i][k] = dp[i][k-1]
        # for d in dp:
        #     print(d)
        # print('')
    print(dp[N][K])


if __name__ == '__main__':
    main()


'''
個数、重量上限
重量
価値
7 2500
300	500	200	600	900 1360 800 250
400	250 980 340 670 780 570 800

7 2500
300	500	200	600	900 1360 800 250
400	250 980 340 670 780 570 800
'''