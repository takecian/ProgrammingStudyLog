# https://atcoder.jp/contests/aising2019/tasks/aising2019_c


H, W = map(int, input().split())

S = []
flag_map = [[False] * W] * H

for _ in range(H):
    s = list(input())
    S.append(s)


def count_root(x, y):
    flag_map[x][y] = True

    root = 0
    expected = '#' if S[x][y] == '.' else '.'

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for di in directions:
        next_x = x + di[0]
        next_y = y + di[1]

        if 0 <= next_x < W and 0 <= next_y < H:
            if flag_map[next_x][next_y] is False and S[next_x][next_y] == expected:
                print('find:' + str(next_x) + ', ' + str(next_y))
                root = 1 + count_root(next_x, next_y)
    return root


answer_root = 0

# for i in range(H):
#     print(S[i])
#     print(flag_map[i])

print(S)
print(flag_map)

for i in range(H):
    for j in range(W):
        answer_root += count_root(i, j)

print(answer_root)

