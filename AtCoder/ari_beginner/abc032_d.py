# https://abc032.contest.atcoder.jp/tasks/abc032_d

N, W = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j < items[i][1]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - items[i][1]] + items[i][0])

    # for d in dp:
    #     print(d)
    # print("------")

print(dp[N][W])
