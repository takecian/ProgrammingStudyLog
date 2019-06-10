# https://atcoder.jp/contests/abc129/tasks/abc129_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop
import copy

def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        w = list(input())
        grid.append(w)

    # w_grid = copy.deepcopy(grid)
    # h_grid = copy.deepcopy(grid)
    w_grid = [[0] * W for _ in range(H)]
    h_grid = [[0] * W for _ in range(H)]

    for h in range(H):
        counter = 0
        for w in range(W):
            if grid[h][w] != '#':
                counter += 1
                w_grid[h][w] = counter
            else:
                counter = 0
                w_grid[h][w] = '#'

    for h in range(H):
        counter = 0
        for w in range(W-1, -1, -1):
            if w_grid[h][w] == '#':
                counter = 0
                continue

            if counter == 0:
                counter = w_grid[h][w]
            else:
                w_grid[h][w] = counter

    for w in range(W):
        counter = 0
        for h in range(H):
            if grid[h][w] != '#':
                counter += 1
                h_grid[h][w] = counter
            else:
                counter = 0
                h_grid[h][w] = '#'

    for w in range(W):
        counter = 0
        for h in range(H-1, -1, -1):
            if h_grid[h][w] == '#':
                counter = 0
                continue

            if counter == 0:
                counter = h_grid[h][w]
            else:
                h_grid[h][w] = counter

    # print(w_grid)
    # print(h_grid)

    # print(w_query)
    def count(i, j):
        h_val = h_grid[i][j]
        w_val = w_grid[i][j]
        val = h_val + w_val
        if h_val > 0 and w_val > 0:
            val -= 1
        return val

    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] != '#':
                # print('h = {}, w = {}, count = {}'.format(h, w, count(h, w)))
                ans = max(ans, count(h, w))
                pass
    print(ans)


if __name__ == '__main__':
    main()
