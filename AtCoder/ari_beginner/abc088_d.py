# https://atcoder.jp/contests/abc088/tasks/abc088_d

H, W = map(int, input().split())
s = [input() for _ in range(H)]
d = [[-1] * W for _ in range(H)]

# 0,0 to h-1, w-1
d[0][0] = 0

queue = []
queue.append([0, 0])

while len(queue) > 0:
    p = queue.pop(0)
    y, x = p[0], p[1]

    dx4 = [0, 0, 1, -1]
    dy4 = [1, -1, 0, 0]

    for dx, dy in zip(dx4, dy4):
        next_y = y + dy
        next_x = x + dx
        if 0 <= next_y < H and 0 <= next_x < W and s[next_y][next_x] != "#" and d[next_y][next_x] == -1:
            d[next_y][next_x] = d[y][x] + 1
            queue.append([next_y, next_x])

count = 0
for l in s:
    for c in l:
        if c == ".":
            count += 1

if d[H-1][W-1] == -1:
    print(-1)
else:
    print(count - d[H-1][W-1] - 1)

# [print(l) for l in s]
# [print(l) for l in d]
