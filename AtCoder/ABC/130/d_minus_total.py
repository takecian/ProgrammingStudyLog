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
    # K 未満の部分列の数を計算する
    for i in range(N):
        while j < N and total + A[j] < K:
            total += A[j]
            j += 1
        ans += j - i
        total -= A[i]

    # 連続部分列の全通りは N * (N + 1) // 2
    # -> 始点から終点までの数で始点を一つずつずらす
    ans = N*(N+1) // 2 - ans
    print(ans)


if __name__ == '__main__':
    main()
