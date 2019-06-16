# https://atcoder.jp/contests/abc130/tasks/abc130_d
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ac = [0] * (N + 1)
    ac[0] = 0
    for i in range(0, N):
        ac[i + 1] = ac[i] + A[i]

    # print(ac)
    ans = 0

    target = K
    for i in range(N):
        # print(target)
        if i > 0:
            target += A[i - 1]
        index = bisect.bisect_left(ac, target)
        # print(len(ac) - index)
        ans += (len(ac) - index)

    print(ans)

if __name__ == '__main__':
    main()
