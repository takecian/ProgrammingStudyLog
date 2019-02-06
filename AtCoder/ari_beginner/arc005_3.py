
H, W = map(int, input().split())
C = [input() for _ in range(H)]


def find(m):
    for y in range(H):
        for x in range(W):
            if C[y][x] == m:
                return y, x
    return -1, -1


s = find("s")
g = find("g")


def bfs(s, g):
    d = [[3] * W for _ in range(H)]

    d[s[0]][s[1]] = 0

    que = []
    que.append((s[0], s[1], 0))
    while len(que) > 0:
        current = que.pop(0)
        if current[0] == g[0] and current[1] == g[1]:
            # goal reached
            break

        dx4 = [0, 0, 1, -1]
        dy4 = [1, -1, 0, 0]
        for dx, dy in zip(dx4, dy4):
            next_y = current[0] + dy
            next_x = current[1] + dx
            if 0 <= next_y < H and 0 <= next_x < W:
                if C[next_y][next_x] == "#" and d[current[0]][current[1]] < 2 and d[current[0]][current[1]] + 1 < d[next_y][next_x]:
                    que.append((next_y, next_x))
                    d[next_y][next_x] = d[current[0]][current[1]] + 1
                elif C[next_y][next_x] == "." and d[current[0]][current[1]] < d[next_y][next_x]:
                    que.append((next_y, next_x))
                    d[next_y][next_x] = d[current[0]][current[1]]
                elif C[next_y][next_x] == "g":
                    return "YES"

    return "NO"


print(bfs(s, g))

