# https://atcoder.jp/contests/arc080/tasks/arc080_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    ans = [[0] * W for _ in range(H)]

    h = 0
    w = 0
    for i in range(N):
        rest = A[i]
        while rest > 0:
            ans[h][w] = i + 1
            rest -= 1
            if h % 2 == 0:
                if 0 <= w < W - 1:
                        w += 1
                else:
                    h += 1
            else:
                if 0 < w <= W - 1:
                        w -= 1
                else:
                    h += 1

    for h in range(H):
        print(' '.join(map(str, ans[h])))


if __name__ == '__main__':
    main()
