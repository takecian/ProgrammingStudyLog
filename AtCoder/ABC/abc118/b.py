# https://atcoder.jp/contests/abc118/tasks/abc118_b

N, M = map(int, input().split())

ans = {}

for _ in range(N):
    K, *A = list(map(int, input().split()))
    for a in A:
        if a in ans:
            ans[a] += 1
        else:
            ans[a] = 1

count = 0
for k, v in ans.items():
    if v == N:
        count += 1

print(count)
