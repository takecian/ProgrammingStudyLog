# https://atcoder.jp/contests/abc115/tasks/abc115_a

d = int(input())

r = 25 - d

ans = "Christmas"

for _ in range(r):
    ans += " Eve"

print(ans)

