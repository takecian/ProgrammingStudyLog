# https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_c


K, A, B = map(int, input().split())

need_turns = A + 1 + 1  # 交換に必要なターン
first_need_turns = need_turns - 1  # 初回は一枚ぶん少ない

if A + 2 > B or K < first_need_turns:  # 交換せずにビスケットを叩き続ける方が得
    print(1 + K)
    exit()

ans = B  # 一度交換した
K -= (need_turns - 1)

# print("{}, {}".format(K, ans))

while K > 0:
    if ans >= A and K >= 2:
        ans += (B - A) * int(K / 2)
        K = K % 2
    else:
        ans += 1
        K -= 1

print(ans)

#
# dp = [[-1 for _ in range(2)] for _ in range(K + 1)]
#
# dp[0][0] = 1
#
# for k in range(K):
#     if dp[k][1] >= 0:
#         dp[k + 1][0] = max(dp[k][0] + 1, dp[k][1] + B)
#     else:
#         dp[k + 1][0] = dp[k][0] + 1
#     if dp[k][0] >= A:
#         dp[k + 1][1] = max(dp[k][0] - A, dp[k][1] + 1)
#     else:
#         if dp[k][1] >= 0:
#             dp[k + 1][1] = dp[k][1] + 1
#
# # for p in dp:
# #     print(p)
#
# print(max(dp[K][0], dp[K][1]))

# import sys
# sys.setrecursionlimit(10000000)
#
# def do_try(k, b, y):
#     if k > K:
#         return b
#     else:
#         if b >= A and y >= 1:
#             # print("1: k = {}, b = {}".format(k, b))
#             return max(do_try(k + 1, b + 1, y), do_try(k + 1, b - A, y + 1), do_try(k + 1, b + B, y - 1))
#         elif b >= A:
#             # print("2: k = {}, b = {},".format(k, b))
#             return max(do_try(k + 1, b + 1, y), do_try(k + 1, b - A, y + 1))
#         elif y >= 1:
#             # print("3: k = {}, b = {}".format(k, b))
#             return max(do_try(k + 1, b + 1, y), do_try(k + 1, b + B, y - 1))
#         else:
#             # print("4: k = {}, b = {}".format(k, b))
#             return do_try(k + 1, b + 1, y)
#
# print(do_try(0, 0, 0))
#

