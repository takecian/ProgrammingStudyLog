# https://abc015.contest.atcoder.jp/tasks/abc015_4

# WIP

W = int(input())
N, K = map(int, input().split())

A = [0]
B = [0]

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[[0 for _ in range(W + 1)] for _ in range(K + 1)] for _ in range(N + 1)]

print(A)
print(B)

for i in range(1, N + 1):
    for k in range(K):
        if k == 0:
            dp[i][0][0] = B[i]
        else:
            dp[i][k][0] = B[i]

for i in range(1, N + 1):

        dp[i][0][0] = B[i]


print(dp)
