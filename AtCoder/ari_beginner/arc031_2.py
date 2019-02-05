# https://atcoder.jp/contests/arc031/tasks/arc031_2

M = [input() for _ in range(10)]

# count island
island_count = 0
for y in range(10):
    for x in range(10):
        if M[y][x] == "o":
            island_count += 1

# print(island_count)

def check(sy, sx):
    reached = [[False for _ in range(10)] for _ in range(10)]

    def dfs(y, x, is_start):
        if y < 0 or 10 <= y or x < 0 or 10 <= x:
            return 0
        if reached[y][x]:
            return 0
        if not is_start and M[y][x] == "x":
            return 0

        reached[y][x] = True

        sea = 0 if M[y][x] == "x" else 1
        return sea + dfs(y + 1, x, False) + dfs(y - 1, x, False) + dfs(y, x + 1, False) + dfs(y, x - 1, False)

    count = dfs(sy, sx, True)
    return island_count == count


for y in range(10):
    for x in range(10):
        if check(y, x):
            print("YES")
            exit()

print("NO")

