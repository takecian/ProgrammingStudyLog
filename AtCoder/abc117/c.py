# https://atcoder.jp/contests/abc117/tasks/abc117_c

N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

if N >= M:
    print("0")
    exit()

# print(X)
diffs = []
for i in range(len(X)-1):
    diffs.append(X[i+1] - X[i])

diffs.sort(reverse=True)

print(sum(diffs[N-1:]))

