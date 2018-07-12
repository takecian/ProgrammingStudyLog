# https://abc032.contest.atcoder.jp/tasks/abc032_d

# TLE

N, W = map(int, input().split())

v = [0]
w = [0]

for _ in range(N):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

# print(v)
# print(w)
# print(dp)

for i in range(1, N + 1):
    for j in range(W + 1):
        if w[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][W])
