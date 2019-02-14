# https://atcoder.jp/contests/abc113/tasks/abc113_b

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))


ans = 0
min_d = 50000
for i in range(N):
    t = T - H[i] * 0.006
    d = abs(A - t)
    if d < min_d:
        min_d = d
        ans = i + 1

print(ans)
