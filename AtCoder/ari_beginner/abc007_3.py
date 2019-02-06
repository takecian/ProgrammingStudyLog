# https://atcoder.jp/contests/abc007/tasks/abc007_3

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

c = [input() for _ in range(R)]

distance = [[-1 for _ in range(C)] for _ in range(R)]
distance[sy][sx] = 0

queue = []
queue.append((sy, sx))

while len(queue) > 0:
    p = queue.pop(0)
    y, x = p[0], p[1]

    dx4 = [0, 0, 1, -1]
    dy4 = [1, -1, 0, 0]
    for dx, dy in zip(dx4, dy4):
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < C and 0 <= next_y < R and c[next_y][next_x] != "#" and distance[next_y][next_x] == -1:
            distance[next_y][next_x] = distance[y][x] + 1
            queue.append((next_y, next_x))

# [print(d) for d in distance]

print(distance[gy][gx])
