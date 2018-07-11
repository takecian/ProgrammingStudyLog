# https://abc015.contest.atcoder.jp/tasks/abc015_4

W = int(input())
N, K = map(int, input().split())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0] * (W + 1) for _ in range(N + 1)]

print(A)
print(B)

print(dp)
