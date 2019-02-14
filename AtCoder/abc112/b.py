# https://atcoder.jp/contests/abc112/tasks/abc112_b

N, T = map(int, input().split())

cts = [list(map(int, input().split())) for _ in range(N)]


cs = []
for ct in cts:
    if ct[1] <= T:
        cs.append(ct)

if len(cs) == 0:
    print("TLE")
    exit()

ans = 1000

for c in cs:
    ans = min(ans, c[0])

print(ans)

