# https://atcoder.jp/contests/abc115/tasks/abc115_d

N, X = map(int, input().split())

l = [1]
p = [1]

for i in range(N):
    l.append(l[i] * 2 + 3)  # 各レベルの長さ
    p.append(p[i] * 2 + 1)  # 各レベルのパティの数


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + l[n-1]:
        return f(n-1,x-1)
    else:
        return p[n-1] + 1 + f(n-1, x-2-l[n-1])


print(f(N, X))

# 愚直に計算したら計算量は大したことないけどメモリが足りなくなる
# dp = ["" for _ in range(N+1)]
# dp[0] = "P"
#
# for i in range(N):
#     dp[i + 1] = "B" + dp[i] + "P" + dp[i] + "B"
#
# print(dp[N])
# # print(dp[N][:X].count("P"))
