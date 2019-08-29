# https://atcoder.jp/contests/abc102/tasks/arc100_b

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    al = list(map(int, input().split()))

    l, c, r = 1, 2, 3
    P = sum(al[:l])
    Q = sum(al[l:c])
    R = sum(al[c:r])
    S = sum(al[r:])

    ans = max(P, Q, R, S) - min(P, Q, R, S)

    while c <= n - 2:
        while True:
            if l == c - 1:
                break
            if abs(P - Q) < abs((P + al[l]) - (Q - al[l])):  # これ以上差が縮まらないなら break
                break

            P += al[l]
            Q -= al[l]
            l += 1

        while True:
            if r == n - 1:
                break
            if abs(R - S) < abs((R + al[r]) - (S - al[r])): # これ以上差が縮まらないなら break
                break

            R += al[r]
            S -= al[r]
            r += 1

        ans = min(max(P, Q, R, S) - min(P, Q, R, S), ans)

        # center を一つ右に進める
        Q += al[c]
        R -= al[c]
        c += 1

    print(ans)

if __name__ == '__main__':
    main()
