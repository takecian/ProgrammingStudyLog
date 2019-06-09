# https://atcoder.jp/contests/abc129/tasks/abc129_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        w = list(input())
        grid.append(w)

    def down(i, j):
        val = 0
        pos = i - 1
        while pos >= 0:
            if grid[pos][j] != '#':
                val += 1
            else:
                break
            pos -= 1

        return val

    def up(i, j):
        val = 0
        pos = i + 1
        while pos < H:
            if grid[pos][j] != '#':
                val += 1
            else:
                break
            pos += 1

        return val

    def left(i, j):
        val = 0
        pos = j - 1
        while pos >= 0:
            if grid[i][pos] != '#':
                val += 1
            else:
                break
            pos -= 1

        return val

    def right(i, j):
        val = 0
        pos = j + 1
        while pos < W:
            if grid[i][pos] != '#':
                val += 1
            else:
                break
            pos += 1

        return val

    def count(i, j):
        return 1 + down(i, j) + up(i, j) + right(i, j) + left(i, j)

    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] != '#':
                ans = max(ans, count(h, w))
    print(ans)


if __name__ == '__main__':
    main()
