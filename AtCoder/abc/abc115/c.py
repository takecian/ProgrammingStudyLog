# https://atcoder.jp/contests/abc115/tasks/abc115_c

N, K = map(int, input().split())

h = [int(input()) for _ in range(N)]

h.sort()

ans = int(1e15)

# print(h)

for i in range(N - K + 1):
    ans = min(ans, h[i + K - 1]-h[i])

print(ans)
