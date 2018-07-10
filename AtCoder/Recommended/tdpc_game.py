# https://tdpc.contest.atcoder.jp/tasks/tdpc_game

A, B = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

dp = [[0 for x in range(B + 1)] for y in range(A + 1)]

for i in range(A + 1):
    for j in range(B + 1):
        if (A + B + i + j) % 2 == 0: # sente
            if i == j == 0:
                dp[i][j] = 0
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + b[B - j]
            elif i != 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + a[A - i]
            else:
                dp[i][j] = max(
                    dp[i][j - 1] + b[B - j],
                    dp[i - 1][j] + a[A - i]
                )
        else: # gote
            if i == j == 0:
                dp[i][j] = 0
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1]
            elif i != 0 and j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(
                    dp[i][j - 1],
                    dp[i - 1][j]
                )

print(dp[A][B])