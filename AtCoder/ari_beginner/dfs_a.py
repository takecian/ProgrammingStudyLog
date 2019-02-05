# https://atc001.contest.atcoder.jp/tasks/dfs_a
import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

checked = [[False for _ in range(W)] for _ in range(H)]


def dfs(h, w):
    if h < 0 or H <= h or w < 0 or W <= w:
        return False
    if C[h][w] == "#":
        return False
    if checked[h][w]:
        return False

    checked[h][w] = True
    if C[h][w] == "g":
        return True

    tmp1 = dfs(h - 1, w)
    tmp2 = dfs(h + 1, w)
    tmp3 = dfs(h, w - 1)
    tmp4 = dfs(h, w + 1)
    return tmp1 or tmp2 or tmp3 or tmp4


for h in range(H):
    for w in range(W):
        if C[h][w] == "s":
            if dfs(h, w):
                print("Yes")
            else:
                print("No")
