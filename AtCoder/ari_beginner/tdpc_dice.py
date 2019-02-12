# https://tdpc.contest.atcoder.jp/tasks/tdpc_dice

N, D = map(int, input().split())

p = [0, 0, 0]
d = [2, 3, 5]
for i in range(3):
    while D % d[i] == 0:
        p[i] += 1
        D = int(D/d[i])

if D > 1:
    print("0")
    exit()

p2 = p[0]
p3 = p[1]
p5 = p[2]

dp = [[[[0 for _ in range(p5 + 1)] for _ in range(p3 + 1)] for _ in range(p2 + 1)] for _ in range(N + 1)]
dp[0][0][0][0] = 1

for i in range(N):
    for j in range(p2 + 1):
        for k in range(p3 + 1):
            for l in range(p5 + 1):
                per = dp[i][j][k][l] / 6
                dp[i + 1][j][k][l] += per  # 1
                dp[i + 1][min(j + 1, p2)][k][l] += per  # 2
                dp[i + 1][j][min(k + 1, p3)][l] += per  # 3
                dp[i + 1][min(j + 2, p2)][k][l] += per  # 4
                dp[i + 1][j][k][min(l + 1, p5)] += per  # 5
                dp[i + 1][min(j + 1, p2)][min(k + 1, p3)][l] += per  # 6

print(dp[N][p2][p3][p5])
