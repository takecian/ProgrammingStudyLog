# https://abc096.contest.atcoder.jp/tasks/abc096_c

neighbor_i = [-1, 0, 1, 0]
neighbor_j = [0, -1, 0, 1]

H, W = map(int, input().split())


def can_draw(l, target_i, target_j):
    for i, j in zip(neighbor_i, neighbor_j):
        if target_i + i < 0 or target_j < 0:
            continue
        if target_i + i >= H or target_j + j >= W:
            continue
        if l[target_i + i][target_j + j] == '#':
            return True

    return False


data = []
for i in range(H):
    raw = list(str(input()))
    data.append(raw)


# print(data)


ok = True
for i in range(H):
    for j in range(W):
        if data[i][j] == '#':
            if not can_draw(data, i, j):
                ok = False
                break
    if not ok:
        break

if ok:
    print('Yes')
else:
    print('No')

