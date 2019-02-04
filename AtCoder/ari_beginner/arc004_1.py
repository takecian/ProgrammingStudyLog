# https://arc004.contest.atcoder.jp/tasks/arc004_1
import math

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

# print(p)

answer = 0
for i in range(len(p)):
    for j in range(1, len(p)):
        answer = max(answer, math.sqrt((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2))

print(answer)
