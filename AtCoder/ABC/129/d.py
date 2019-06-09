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

    h_path = [[] for _ in range(H)]
    for h in range(H):
        c = 0
        for w in range(W):
            if grid[h][w] == '#':
                if c > 0:
                    h_path[h].append(c)
                    c = 0
                h_path[h].append(0)
            else:
                c += 1
        if c > 0:
            h_path[h].append(c)
    # print(h_path)

    h_query = [[0] * W for _ in range(H)]
    for h in range(H):
        path = h_path[h]
        index = 0
        for p in path:
            l = p if p > 0 else 1
            while l > 0:
                h_query[h][index] = p
                l -= 1
                index += 1

    # print(h_query)

    w_path = [[] for _ in range(W)]
    for w in range(W):
        c = 0
        for h in range(H):
            if grid[h][w] == '#':
                if c > 0:
                    w_path[w].append(c)
                    c = 0
                w_path[w].append(0)
            else:
                c += 1
        if c > 0:
            w_path[w].append(c)
    # print(w_path)

    w_query = [[0] * W for _ in range(H)]
    for w in range(W):
        path = w_path[w]
        index = 0
        for p in path:
            l = p if p > 0 else 1
            while l > 0:
                w_query[index][w] = p
                l -= 1
                index += 1

    # print(h_query)
    # print(w_query)
    def count(i, j):
        h_val = h_query[i][j]
        w_val = w_query[i][j]
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
