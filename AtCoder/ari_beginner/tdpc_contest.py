# https://tdpc.contest.atcoder.jp/tasks/tdpc_contest

N = int(input())
P = list(map(int, input().split()))

p_sum = sum(P)

dp = [[False for _ in range(p_sum + 1)] for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(p_sum + 1):
        if j - P[i] < 0:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j] or dp[i][j - P[i]]

# print(dp)
c = dp[N].count(True)
# for v in dp[N]:
#     if v > 0:
#         c += 1

print(c)
