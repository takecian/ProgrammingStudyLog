# https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_d

L = int(input())

A = [int(input()) for _ in range(L)]

INF = int(1e15)
dp = [[INF] * (L + 1) for _ in range(5)]

for i in range(4):
    dp[i][0] = 0

for i in range(L):
    dp[0][i + 1] = dp[0][i] + A[i]  # 全部取り除く
    dp[1][i + 1] = min(dp[j][i] for j in range(2)) + (A[i] % 2 if A[i] != 0 else 2)
    dp[2][i + 1] = min(dp[j][i] for j in range(3)) + (1 if A[i] % 2 == 0 else 0)
    dp[3][i + 1] = min(dp[j][i] for j in range(4)) + (A[i] % 2 if A[i] != 0 else 2)
    dp[4][i + 1] = min(dp[j][i] for j in range(5)) + A[i]  # 全部取り除く


print(min(dp[i][L] for i in range(1, 5)))
