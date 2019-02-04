# https://atcoder.jp/contests/abc075/tasks/abc075_b

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def is_bomb(x, y):
    return S[y][x] == "#"

def count_neibor(x, y):
    dxs = [1, -1, 0, 0, 1, 1, -1, -1]
    dys = [0, 0, 1, -1, 1, -1, 1, -1]
    count = 0
    for dx, dy in zip(dxs, dys):
        check_x = x + dx
        check_y = y + dy
        if 0 <= check_x < W and 0 <= check_y < H:
            count += 1 if S[check_y][check_x] == "#" else 0
    return count

result = []
for y in range(H):
    row = []
    for x in range(W):
        if is_bomb(x, y):
            row.append("#")
        else:
            row.append(str(count_neibor(x, y)))
    result.append(row)

for c in result:
    print(''.join(c))

