# https://atcoder.jp/contests/abc083/tasks/arc088_a

X, Y = map(int, input().split())

start = X

ans = []
t = X
while t <= Y:
    ans.append(t)
    t *= 2

print(len(ans))
