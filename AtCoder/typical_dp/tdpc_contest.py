# https://tdpc.contest.atcoder.jp/tasks/tdpc_contest

N = int(input())
P = [int(i) for i in input().split()]

# # Case 1
# L = [set() for _ in range(N+1)]
#
# L[0].add(0)
# for i in range(1, N+1):
#     for a in L[i-1]:
#         L[i].add(a)
#         L[i].add(a+P[i-1])
#
# print(len(L[N]))

# Case 2
# cache = {}
# def can_make(n, val):
#     if n in cache and val in cache[n]:
#         return cache[n][val]
#
#     if n == 0:
#         return val == 0
#
#     if val - P[n - 1] < 0:
#         if can_make(n - 1, val):
#             if n in cache:
#                 cache[n][val] = True
#             else:
#                 cache[n] = {val: True}
#             return True
#         else:
#             if n in cache:
#                 cache[n][val] = False
#             else:
#                 cache[n] = {val: False}
#             return False
#     else:
#         if can_make(n - 1, val - P[n - 1]) or can_make(n - 1, val):
#             if n in cache:
#                 cache[n][val] = True
#             else:
#                 cache[n] = {val: True}
#             return True
#         else:
#             if n in cache:
#                 cache[n][val] = False
#             else:
#                 cache[n] = {val: False}
#             return False
#
# ans = 0
# s = sum(P)
#
# for i in range(s + 1):
#     if can_make(N, i):
#         ans += 1
#
# print(ans)

# Case 3
S = sum(P)
dp = [[0 for y in range(S + 1)] for x in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(S + 1):
        if j - P[i-1] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - P[i - 1]]

print(dp)
c = 0
for v in dp[N]:
    if v > 0:
        c += 1

print(c)
