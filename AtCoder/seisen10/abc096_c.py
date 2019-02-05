# https://atcoder.jp/contests/abc096/tasks/abc096_c

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 隣に # が一つ以上あるかどうか
def has_neighbor(y, x):
    dhs = [1, -1, 0, 0]
    dws = [0, 0, 1, -1]
    for dh, dw in zip(dhs, dws):
        if 0 <= y + dh < H and 0 <= x + dw < W:
            if S[y + dh][x + dw] == "#":
                return True
    return False


for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            if not has_neighbor(h, w):
                print("No")
                exit()

print("Yes")
