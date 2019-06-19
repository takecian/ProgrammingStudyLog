# https://atcoder.jp/contests/abc130/tasks/abc130_d
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0

    total = 0
    j = 0
    # 始点をずらしつつ K 以上の部分列の数を計算する
    for i in range(N):
        while j < N and total < K:
            total += A[j]
            j += 1
        if total >= K:
            # print(N - j + 1)
            ans += N - j + 1
        total -= A[i]

    print(ans)


if __name__ == '__main__':
    main()
